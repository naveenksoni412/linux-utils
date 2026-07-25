#!/bin/bash

# Target only processes that originate from the Citrix installation path
# -f matches against the full command line (including the path)
# -u $USER ensures we only kill your own processes, not other users
FILE=$1
pkill -9 -u $USER -f "/opt/Citrix/ICAClient/"

# A small delay to let the OS clean up the process table/sockets
sleep 0.5

# Launch the new session using the absolute path to the engine
#/opt/Citrix/ICAClient/wfica.sh "$1"
notify-send "Citrix Launched" "location of ica file: $FILE"

/opt/Citrix/ICAClient/adapter -icaroot /opt/Citrix/ICAClient "$FILE"
