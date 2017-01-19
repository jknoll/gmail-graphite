#!/usr/bin/env python
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
