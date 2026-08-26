#!/usr/bin/env bash
# UNIX Shell script to set up Python environment variables

echo "Execute using \`source setup_py_env.sh\`"

# Resolve the absolute path of the directory containing this script
PROJ_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Prepend project directories to PYTHONPATH while preserving existing paths
export PYTHONPATH="${PROJ_DIR}:${PROJ_DIR}/src:${PROJ_DIR}/tests:${PYTHONPATH}"