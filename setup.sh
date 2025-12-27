#!/bin/bash
# Configuration
COMMAND_NAME="zxt" # The name users will type in terminal 
PY_FILE="$(pwd)/main.py" 
echo "Setting up $COMMAND_NAME for Unix-like system..." 
# 1. Validation
if [ ! -f "$PY_FILE" ]; then 
echo "Error: main.py not found in $(pwd)" 
exit 1 
fi
# 2. Permissions & Linking
chmod +x "$PY_FILE" 
sudo ln -sf "$PY_FILE" "/usr/local/bin/$COMMAND_NAME" 
# 3. Cleanup
if [ -f "setup.ps1" ]; then 
rm "setup.ps1" 
echo "Cleaned up Windows setup files." 
fi 
echo "Done! Try running: $COMMAND_NAME" 
