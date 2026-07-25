#!/bin/bash
# Restore Ubuntu MATE settings, themes, and packages

BACKUP_DIR=~/Documents/mate-backup

echo "🔄 Restoring themes and icons..."
tar -xzf "$BACKUP_DIR/themes-icons.tar.gz" -C ~/
tar -xzf "$BACKUP_DIR/wallpapers.tar.gz" -C ~/
tar -xzf "$BACKUP_DIR/local-share.tar.gz" -C ~/
tar -xzf "$BACKUP_DIR/mate-config.tar.gz" -C ~/

echo "🔄 Restoring system-wide themes and icons (requires sudo)..."
sudo tar -xzf "$BACKUP_DIR/usr-share-themes-icons.tar.gz" -C /

echo "🔄 Restoring dconf (panels, indicators, themes)..."
dconf load / < "$BACKUP_DIR/dconf-settings.conf"

echo "🔄 Restoring package list..."
sudo dpkg --set-selections < "$BACKUP_DIR/package-list.txt"
sudo apt-get -y dselect-upgrade

echo "✅ Restore complete. Please log out and log back in (or reboot)."

