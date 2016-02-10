#!/usr/bin/env bash

# Stop and unload the launchctl service if running
launchctl stop com.justinknoll.graphite.fullcount
launchctl unload ~/Documents/git/gmail-graphite/com.justinknoll.graphite.fullcount.plist

# Load and start the launchctl service
launchctl load ~/Documents/git/gmail-graphite/com.justinknoll.graphite.fullcount.plist
launchctl start com.justinknoll.graphite.fullcount