#!/usr/bin/env bash
# Creates .venv (if missing) and installs/updates dependencies.
set -euo pipefail
cd "$(dirname "$0")/.."

PYTHON="${PYTHON:-python3}"

if [ ! -d ".venv" ]; then
  echo "Creating virtual environment in .venv ..."
  "$PYTHON" -m venv .venv
fi

# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements/dev.txt

echo
echo "Done. Activate with: source .venv/bin/activate"
