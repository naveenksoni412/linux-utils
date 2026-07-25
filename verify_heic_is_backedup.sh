#!/bin/bash

# Usage: ./move_matched_heic.sh /path/to/folder

if [ $# -ne 1 ]; then
    echo "Usage: $0 /path/to/folder"
    exit 1
fi

folder="$1"
temp_folder="$folder/temp"

mkdir -p "$temp_folder"

shopt -s nocaseglob

cd "$folder" || exit 1

for heic_file in *.HEIC *.heic; do
    # Skip if no matches
    [ -e "$heic_file" ] || continue

    base="${heic_file%.*}"
    
    # Check if a matching .jpg or .JPG file exists
    if ls "${base}".jpg >/dev/null 2>&1 || ls "${base}".JPG >/dev/null 2>&1; then
        echo "Moving $heic_file to $temp_folder"
        mv "$heic_file" "$temp_folder/"
    fi
done

