#!/usr/bin/env python3

import os
import subprocess
import logging
import gi

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3, GLib

# Setup logging
LOG_FILE = os.path.expanduser("~/.local/share/headset_keepalive.log")
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Config
SILENT_FILE = "/home/naveenksoni411/HailTheAlmighty/linux-utils/silence.wav"
DESKTOP_FILE = "/home/naveenksoni411/.local/share/applications/keep-headset-alive.desktop"
ICON_ON = "/home/naveenksoni411/icons/headset-on.png"
ICON_OFF = "/home/naveenksoni411/icons/headset-off.png"

APP_ID = "headset.keepalive"


class HeadsetTrayApp:
    def __init__(self):
        self.indicator = AppIndicator3.Indicator.new(
            APP_ID,
            ICON_OFF,
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        self.update_icon()

    def build_menu(self):
        menu = Gtk.Menu()

        toggle_item = Gtk.MenuItem(label="Toggle Headset")
        toggle_item.connect("activate", self.toggle_state)
        menu.append(toggle_item)

        quit_item = Gtk.MenuItem(label="Quit")
        quit_item.connect("activate", self.quit)
        menu.append(quit_item)

        menu.show_all()
        return menu

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
            stderr=subprocess.DEVNULL,
        )
        logging.info("Started keepalive")

    def stop_keepalive(self):
        subprocess.call("pkill -f 'mpv.*silence'", shell=True)
        logging.info("Stopped keepalive")

    def set_desktop_icon(self, path):
        try:
            if not os.path.exists(DESKTOP_FILE):
                return
            with open(DESKTOP_FILE, "r") as f:
                lines = f.readlines()
            with open(DESKTOP_FILE, "w") as f:
                for line in lines:
                    if line.startswith("Icon="):
                        f.write(f"Icon={path}\n")
                    else:
                        f.write(line)
            subprocess.call(
                ["update-desktop-database", os.path.expanduser("~/.local/share/applications/")]
            )
        except Exception as e:
            logging.error(f"Failed to update .desktop icon: {e}")

    def update_icon(self):
        if self.is_alive():
            self.indicator.set_icon_full(ICON_ON, "Headset active")
            self.set_desktop_icon(ICON_ON)
        else:
            self.indicator.set_icon_full(ICON_OFF, "Headset inactive")
            self.set_desktop_icon(ICON_OFF)

    def toggle_state(self, *args):
        if self.is_alive():
            self.stop_keepalive()
        else:
            self.start_keepalive()
        self.update_icon()

    def quit(self, widget):
        Gtk.main_quit()


# Run the app
if __name__ == "__main__":
    app = HeadsetTrayApp()
    GLib.threads_init()
    Gtk.main()
