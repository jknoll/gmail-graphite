#!/usr/bin/env python
import feedparser
import socket
from config import config

def get_count(url):
    d = feedparser.parse(url)
    fullcount = d['feed']['fullcount']
    return fullcount

def send_count(count):
    message = config['graphite_prefix'] + " %s\n" % count
    conn = socket.create_connection((config['graphite_host'], config['graphite_port']))
    conn.send(message)
    conn.close()

def process():
    count = get_count(config['gmail_feed_url'])
    send_count(count)

if __name__ == "__main__":
    process()
