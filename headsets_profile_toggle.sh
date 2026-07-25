#!/bin/bash
# 1. Identify the EPOS device ID (it changes, so we grep for it)
EPOS_ID=$(wpctl status | grep -i "EPOS BTD 800 III" | grep "alsa" | awk '{print $2}' | tr -d '.')

if [ -z "$EPOS_ID" ]; then
    notify-send "EPOS Fix" "Dongle not found!" --icon=audio-speakers
    exit 1
fi

# 2. Force it to 'off' then back to 'pro-audio' (The Nudge)
wpctl set-profile "$EPOS_ID" 2
sleep 0.5
wpctl set-profile "$EPOS_ID" 5

notify-send "EPOS Fixed" "Pro Audio profile re-synced. epos id: $EPOS_ID" --icon=audio-headset
