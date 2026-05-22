#!/usr/bin/env bash
# Compile DumpSemantics.java against the vendored tla2tools.jar.
# Use: ./build.sh                  -> just compile
#      ./run.sh <input.tla>        -> compile (if needed) and run.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"
TLA2TOOLS="$REPO_ROOT/lib/tla2tools.jar"
if [[ ! -f "$TLA2TOOLS" ]]; then
  echo "error: $TLA2TOOLS not found — run scripts/install_deps.sh first" >&2
  exit 1
fi
BUILD="$SCRIPT_DIR/build"
mkdir -p "$BUILD"
javac -cp "$TLA2TOOLS" -d "$BUILD" "$SCRIPT_DIR/DumpSemantics.java"
echo "built: $BUILD/DumpSemantics.class"
