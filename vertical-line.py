#!/usr/bin/env python
# Usage:
# Send an event named "personal.events.test with the current timestamp as
# follows:
# $ ./vertical-line.py personal.events.test
# Then view it overlaid on another metric using &target=drawAsInfinite():
#
# https://www.hostedgraphite.com/f4edeeed/graphite/render/?width=600&
# height=300&_salt=1351370988.386&lineWidth=2&areaMode=first&
# areaAlpha=0.8&from=-2hours&graphOnly=false&
# target=keepLastValue(personal.email.bittorrent.fullcount)&
# target=drawAsInfinite(personal.events.test)&yMin=0
import socket
from sys import argv
from config import config

def send_message(stat_name, value):
    message = config['graphite_api_key'] + "." + stat_name + " %s\n" % value
    conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
    conn.send(message)
    conn.close()

if __name__ == "__main__":
    if 2 == len(argv):
        send_message(argv[1], 1)
    else:
        print "Usage: ./vertical-line.py [metric-name]"
