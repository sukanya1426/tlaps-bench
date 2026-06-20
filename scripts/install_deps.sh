#!/usr/bin/env bash
# Install host-side dependencies for tlaps-bench:
#   - tlapm 1.6 pre-release  -> ~/.tlapm
#   - Apalache 0.57.0        -> ~/.apalache
#   - tla2tools.jar (SANY)   -> <repo>/lib/tla2tools.jar
#
# Idempotent: skips downloads when the target is already present.
# Docker installs are handled inside docker/Dockerfile and are not touched here.

set -euo pipefail

# Pinned versions — bump deliberately, then re-run.
# 1.6.0-pre is a *rolling* tag (the asset is rebuilt in place), so the tag alone
# is not reproducible — pin by the expected `tlapm --version` commit and
# re-download on mismatch. 80172c6 is the first rolling build carrying `--strict`
# (tlaplus/tlapm#278); bump TLAPM_COMMIT deliberately when upgrading.
TLAPM_TAG="1.6.0-pre"
TLAPM_COMMIT="80172c6"
TLAPM_ASSET="tlapm-${TLAPM_TAG}-x86_64-linux-gnu.tar.gz"
TLAPM_URL="https://github.com/tlaplus/tlapm/releases/download/${TLAPM_TAG}/${TLAPM_ASSET}"

APALACHE_TAG="v0.57.0"
APALACHE_VERSION="${APALACHE_TAG#v}"
APALACHE_ASSET="apalache-${APALACHE_VERSION}.tgz"
APALACHE_URL="https://github.com/apalache-mc/apalache/releases/download/${APALACHE_TAG}/${APALACHE_ASSET}"

TLATOOLS_TAG="v1.8.0"
TLATOOLS_URL="https://github.com/tlaplus/tlaplus/releases/download/${TLATOOLS_TAG}/tla2tools.jar"

COMMUNITY_TAG="202604221529"
COMMUNITY_URL="https://github.com/tlaplus/CommunityModules/archive/refs/tags/${COMMUNITY_TAG}.tar.gz"

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LIB_DIR="${REPO_ROOT}/lib"

# --- tlapm ---
# Pin by commit, not mere presence: the rolling tag means an existing ~/.tlapm
# may be an older build (e.g. one without --strict), so re-install on mismatch.
if [[ -x "${HOME}/.tlapm/bin/tlapm" ]] \
   && "${HOME}/.tlapm/bin/tlapm" --version 2>/dev/null | grep -q "${TLAPM_COMMIT}"; then
  echo "[install_deps] tlapm ${TLAPM_COMMIT} already at ~/.tlapm — skipping"
else
  echo "[install_deps] installing tlapm ${TLAPM_TAG} (${TLAPM_COMMIT})..."
  curl -fsSL -o "/tmp/${TLAPM_ASSET}" "${TLAPM_URL}"
  rm -rf "${HOME}/.tlapm" "${HOME}/tlapm"
  tar -xzf "/tmp/${TLAPM_ASSET}" -C "${HOME}/" # extracts to ~/tlapm/
  mv "${HOME}/tlapm" "${HOME}/.tlapm"
  rm -f "/tmp/${TLAPM_ASSET}"
  rm -f "${HOME}/.tlapm/bin/tlapm_lsp" 2>/dev/null || true
  installed="$("${HOME}/.tlapm/bin/tlapm" --version 2>/dev/null | head -1 || true)"
  if ! echo "${installed}" | grep -q "${TLAPM_COMMIT}"; then
    echo "[install_deps] WARNING: tlapm version '${installed}' != expected ${TLAPM_COMMIT};" >&2
    echo "[install_deps]          the rolling 1.6.0-pre asset has moved — bump TLAPM_COMMIT." >&2
  fi
fi

# --- Apalache ---
if [[ -x "${HOME}/.apalache/bin/apalache-mc" ]]; then
  echo "[install_deps] Apalache already at ~/.apalache — skipping"
else
  echo "[install_deps] downloading Apalache ${APALACHE_TAG}..."
  curl -fsSL -o "/tmp/${APALACHE_ASSET}" "${APALACHE_URL}"
  rm -rf "${HOME}/.apalache" "${HOME}/apalache-${APALACHE_VERSION}"
  tar -xzf "/tmp/${APALACHE_ASSET}" -C "${HOME}/"  # extracts to ~/apalache-<version>/
  mv "${HOME}/apalache-${APALACHE_VERSION}" "${HOME}/.apalache"
  rm -f "/tmp/${APALACHE_ASSET}"
fi

# --- tla2tools.jar (SANY) ---
mkdir -p "${LIB_DIR}"
if [[ -f "${LIB_DIR}/tla2tools.jar" ]]; then
  echo "[install_deps] tla2tools.jar already at lib/ — skipping"
else
  echo "[install_deps] downloading tla2tools.jar ${TLATOOLS_TAG}..."
  curl -fsSL -o "${LIB_DIR}/tla2tools.jar" "${TLATOOLS_URL}"
fi

# --- CommunityModules (.tla) ---
if [[ -f "${LIB_DIR}/community/SequencesExt.tla" ]]; then
  echo "[install_deps] CommunityModules already at lib/community/ — skipping"
else
  echo "[install_deps] downloading CommunityModules ${COMMUNITY_TAG}..."
  CM_TMP="$(mktemp -d)"
  curl -fsSL -o "${CM_TMP}/community.tar.gz" "${COMMUNITY_URL}"
  tar -xzf "${CM_TMP}/community.tar.gz" -C "${CM_TMP}/"
  mkdir -p "${LIB_DIR}/community"
  cp "${CM_TMP}/CommunityModules-${COMMUNITY_TAG}/modules/"*.tla "${LIB_DIR}/community/"
  rm -rf "${CM_TMP}"
fi

echo "[install_deps] done."
echo
echo "Versions:"
"${HOME}/.tlapm/bin/tlapm" --version | sed 's/^/  tlapm:    /'
"${HOME}/.apalache/bin/apalache-mc" 2>&1 | grep -i version | head -1 | sed 's/^/  apalache: /' || true
java -cp "${LIB_DIR}/tla2tools.jar" tla2sany.SANY 2>&1 | head -1 | sed 's/^/  sany:     /' || true
