# UNIX Shell script to setup the Python environental variables

echo "Execute using \`source setup_py_env.sh\`"
CURRENT_PROJ_DIR=$(pwd)
# echo $CURRENT_PROJ_DIR
export PYTHONPATH="$CURRENT_PROJ_DIR:$CURRENT_PROJ_DIR/src:$CURRENT_PROJ_DIR/tests"