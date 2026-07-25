#!/bin/bash
# Backup Ubuntu MATE settings, themes, and packages

BACKUP_DIR=~/Documents/mate-backup
mkdir -p "$BACKUP_DIR"

echo "🔄 Backing up dconf (panel layouts, themes, indicators)..."
dconf dump / > "$BACKUP_DIR/dconf-settings.conf"

echo "🔄 Backing up MATE configs..."
tar -czf "$BACKUP_DIR/mate-config.tar.gz" ~/.config/mate* 2>/dev/null

echo "🔄 Backing up themes and icons..."
tar -czf "$BACKUP_DIR/themes-icons.tar.gz" ~/.themes ~/.icons 2>/dev/null

echo "🔄 Backing up wallpapers..."
tar -czf --exclude=~/Pictures/temp "$BACKUP_DIR/wallpapers.tar.gz" ~/Pictures ~/.local/share/backgrounds 2>/dev/null

echo "🔄 Backing up local share data..."
tar -czf "$BACKUP_DIR/local-share.tar.gz" ~/.local/share/mate-panel ~/.local/share/applications 2>/dev/null

echo "🔄 Backing up system-wide themes and icons (requires sudo)..."
sudo tar -czf "$BACKUP_DIR/usr-share-themes-icons.tar.gz" /usr/share/themes /usr/share/icons

echo "🔄 Backing up installed package list..."
dpkg --get-selections > "$BACKUP_DIR/package-list.txt"

echo "✅ Backup completed. Files saved in $BACKUP_DIR"

