#!/bin/bash
set -e

DEST_DIR="/usr/share/backgrounds"
SCHEMA_OVERRIDE="/usr/share/glib-2.0/schemas/99_arctica-greeter.gschema.override"

# Check if YAD is installed
if ! command -v yad &>/dev/null; then
    pkexec apt install -y yad
fi

# Ask user to pick an image
IMAGE_PATH=$(yad --file --center --title="Select an image" --width=600 --height=400)
[ -z "$IMAGE_PATH" ] && exit 1

# Validate MIME type
MIME_TYPE=$(file --mime-type -b "$IMAGE_PATH")
if [[ ! $MIME_TYPE =~ ^image/ ]]; then
    yad --title "Error" --center --width=400 --height=100 --button=OK \
        --text "The selected file is not an image."
    exit 1
fi

# Prepare final path
IMAGE_NAME=$(basename "$IMAGE_PATH")
FINAL_IMAGE_PATH="$DEST_DIR/$IMAGE_NAME"

# Copy image with root
pkexec bash -c "
    cp -f \"$IMAGE_PATH\" \"$FINAL_IMAGE_PATH\"
    chmod 644 \"$FINAL_IMAGE_PATH\"

    # Lock screen (MATE uses this common PNG)
    cp -f \"$FINAL_IMAGE_PATH\" /usr/share/backgrounds/ubuntu-mate-common.png

    # Write override schema for Arctica Greeter
    echo \"[org.ArcticaProject.arctica-greeter]
background='$FINAL_IMAGE_PATH'
draw-user-background=false
\" > \"$SCHEMA_OVERRIDE\"

    # Compile schemas
    glib-compile-schemas /usr/share/glib-2.0/schemas/
"

# Set user wallpaper
dconf write /org/mate/desktop/background/picture-filename "'$FINAL_IMAGE_PATH'"

notify-send "Done" "Wallpaper, lock screen, and login screen updated. Please log out to see changes."
echo "All backgrounds updated → $FINAL_IMAGE_PATH"

