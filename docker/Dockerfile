FROM ubuntu:24.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install minimal dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates git python3 \
    libstdc++6 libgmp10 make \
    iptables iproute2 dnsutils gosu \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js 22 (for codex CLI)
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y --no-install-recommends nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install codex CLI
RUN npm install -g @openai/codex && npm cache clean --force

# Install tlapm 1.5 from official release, remove examples
RUN curl -fsSL -o /tmp/tlaps.bin \
    https://github.com/tlaplus/tlapm/releases/download/202210041448/tlaps-1.5.0-x86_64-linux-gnu-inst.bin \
    && chmod +x /tmp/tlaps.bin \
    && /tmp/tlaps.bin -d /opt/tlapm15 \
    && rm /tmp/tlaps.bin \
    && rm -rf /opt/tlapm15/lib/tlaps/examples

# Remove sudo
RUN apt-get purge -y sudo 2>/dev/null; rm -f /usr/bin/sudo /usr/sbin/sudo; true

# Create unprivileged user
RUN useradd -m -s /bin/bash bench

# Copy entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /home/bench

# Start as root for iptables setup, then drop to bench user
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
