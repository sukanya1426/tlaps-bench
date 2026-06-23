# Stage 1: Compile check_proof_bin from source (no source leaks to final image)
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir pyinstaller

COPY pyproject.toml /build/pyproject.toml
COPY src/ /build/src/

RUN cd /build && pyinstaller --onefile --name check_proof_bin \
        --paths src/common --paths src \
        --collect-submodules tlacheck \
        --collect-submodules tlacore \
        src/common/check_proof.py \
    && mv dist/check_proof_bin /check_proof_bin

# Stage 2: Final image (agent runtime)
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# Core dependencies (JDK for SANY compilation)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates git python3 python3-pip \
    libstdc++6 libgmp10 make \
    default-jdk-headless \
    iptables iproute2 dnsutils \
    && rm -rf /var/lib/apt/lists/*

# Node.js 22 (needed by codex/claude/copilot install scripts)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# tlapm 1.6 pre-release
RUN curl -fsSL -o /tmp/tlapm.tar.gz \
    https://github.com/tlaplus/tlapm/releases/download/1.6.0-pre/tlapm-1.6.0-pre-x86_64-linux-gnu.tar.gz \
    && tar -xzf /tmp/tlapm.tar.gz -C /opt/ \
    && rm /tmp/tlapm.tar.gz \
    && rm -f /opt/tlapm/bin/tlapm_lsp \
    && { /opt/tlapm/bin/tlapm --version | grep -q 80172c6 \
         || { echo "ERROR: tlapm rolling asset moved off commit 80172c6" >&2; exit 1; }; }

# CommunityModules into tlapm stdlib
RUN curl -fsSL -o /tmp/community.tar.gz \
    https://github.com/tlaplus/CommunityModules/archive/refs/tags/202604221529.tar.gz \
    && tar -xzf /tmp/community.tar.gz -C /tmp/ \
    && cp /tmp/CommunityModules-202604221529/modules/*.tla /opt/tlapm/lib/tlapm/stdlib/ \
    && rm -rf /tmp/community.tar.gz /tmp/CommunityModules-202604221529

# Lock down tlapm
RUN chown -R root:root /opt/tlapm && chmod -R a-w /opt/tlapm

# Cheat checker (from builder stage — no source in final image)
COPY --from=builder /check_proof_bin /usr/local/bin/check_proof_bin

# SANY assets + compile DumpSemantics inside image
COPY lib/tla2tools.jar /opt/sany/lib/tla2tools.jar
COPY lib/community /opt/sany/lib/community
COPY src/dataset/sany-dump /opt/sany/src/dataset/sany-dump
RUN cd /opt/sany/src/dataset/sany-dump && bash build.sh

ENV SANY_RUN_SH=/opt/sany/src/dataset/sany-dump/run.sh \
    TLAPS_LIB=/opt/tlapm/lib/tlapm/stdlib \
    COMMUNITY_LIB=/opt/sany/lib/community

# Lock down checker + SANY (agent can execute but not read source)
RUN chmod 0755 /usr/local/bin/check_proof_bin \
    && chown -R root:root /usr/local/bin/check_proof_bin /opt/sany \
    && chmod -R a-w /opt/sany

# Install scripts directory
COPY docker/install-scripts /opt/install-scripts
RUN chmod -R +x /opt/install-scripts

# Firewall script
COPY docker/firewall.sh /opt/firewall.sh
RUN chmod +x /opt/firewall.sh

# Entrypoint: run firewall then exec the command
COPY docker/base-entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
