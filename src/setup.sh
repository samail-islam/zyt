#!/bin/bash

# Configuration
COMMAND_NAME="zyt"
BIN_DIR="$HOME/bin"
PY_FILE="$(cd "$(dirname "$0")" && pwd)/main.py"

echo "Installing $COMMAND_NAME for $(uname)..."

# 1. Ensure the private bin directory exists
mkdir -p "$BIN_DIR"

# 2. Make Python script executable and link it
if [ -f "$PY_FILE" ]; then
    chmod +x "$PY_FILE"
    ln -sf "$PY_FILE" "$BIN_DIR/$COMMAND_NAME"
    echo "Linked $COMMAND_NAME to $PY_FILE"
else
    echo "Error: main.py not found at $PY_FILE"
    exit 1
fi

# 3. Add to PATH in the correct profile file
# macOS uses .zshrc by default; most Linux uses .bashrc
if [[ "$SHELL" == */zsh ]]; then
    PROFILE="$HOME/.zshrc"
else
    PROFILE="$HOME/.bashrc"
fi

if [[ ":$PATH:" != *":$BIN_DIR:"* ]]; then
    echo "Updating PATH in $PROFILE..."
    echo "export PATH=\"\$PATH:$BIN_DIR\"" >> "$PROFILE"
    echo "Path updated. Please restart terminal or run: source $PROFILE"
fi

# 4. Self-Destruct Windows setup
[ -f "setup.ps1" ] && rm "setup.ps1" && echo "Removed Windows setup file."

echo "Installation finished successfully!"
