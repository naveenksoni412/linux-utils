#!/usr/bin/env python3

import os
import subprocess
import logging
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GObject

# Setup logging
LOG_FILE = "/var/log/headset_keepalive.log"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s - %(message)s')

# Config
SILENT_FILE = "/home/naveenksoni412/HailTheAlmighty/linux-utils/silence.wav"
DESKTOP_FILE = "/home/naveenksoni412/.local/share/applications/keep-headset-alive.desktop"
ICON_ON = "/home/naveenksoni412/icons/headset-on.png"
ICON_OFF = "/home/naveenksoni412/icons/headset-off.png"

class HeadsetTrayApp:
    def __init__(self):
        self.status_icon = Gtk.StatusIcon()
        self.status_icon.connect("activate", self.toggle_state)
        self.status_icon.connect("popup-menu", self.on_right_click)

        self.menu = Gtk.Menu()

        self.toggle_item = Gtk.MenuItem(label="Toggle Headset")
        self.toggle_item.connect("activate", self.toggle_state)
        self.menu.append(self.toggle_item)

        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit)
        self.menu.append(quit_item)

        self.menu.show_all()
        self.update_icon()

    def is_alive(self):
        try:
            output = subprocess.check_output(
                "ps -eo pid,cmd | grep '[m]pv' | grep silence", shell=True
            )
            return bool(output.strip())
        except subprocess.CalledProcessError:
            return False

    def start_keepalive(self):
        subprocess.Popen(
            ["nohup", "mpv", "--no-video", "--loop-file=inf", "--volume=0", "--really-quiet", SILENT_FILE],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        logging.info("Started keepalive")

    def stop_keepalive(self):
        subprocess.call("pkill -f 'mpv.*silence'", shell=True)
        logging.info("Stopped keepalive")

    def set_desktop_icon(self, path):
        try:
            with open(DESKTOP_FILE, "r") as f:
                lines = f.readlines()
            with open(DESKTOP_FILE, "w") as f:
                for line in lines:
                    if line.startswith("Icon="):
                        f.write(f"Icon={path}\n")
                    else:
                        f.write(line)
            subprocess.call(["update-desktop-database", os.path.expanduser("~/.local/share/applications/")])
        except Exception as e:
            logging.error(f"Failed to update .desktop icon: {e}")

    def update_icon(self):
        if self.is_alive():
            self.status_icon.set_from_file(ICON_ON)
            self.set_desktop_icon(ICON_ON)
        else:
            self.status_icon.set_from_file(ICON_OFF)
            self.set_desktop_icon(ICON_OFF)

    def toggle_state(self, *args):
        if self.is_alive():
            self.stop_keepalive()
        else:
            self.start_keepalive()
        self.update_icon()

    def on_right_click(self, icon, button, time):
        self.menu.popup(None, None, None, None, button, time)

    def quit(self, widget):
        Gtk.main_quit()

# Run the app
if __name__ == "__main__":
    GObject.threads_init()
    app = HeadsetTrayApp()
    Gtk.main()

