#!/usr/bin/env python
import feedparser
import socket
from config import config

# Example URL: https://username@example.org:password@gmail.google.com/mail/feed/atom
def get_count(url):
    d = feedparser.parse('url')
    fullcount = d['feed']['fullcount']
    return fullcount

def send_count(count):
    message = "api_key.personal.email.bittorrent.fullcount %s\n" % count

    conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
    conn.send(message)
    conn.close()

def process():
    count = get_count(config['gmail_feed_url'])
    send_count(count)

if __name__ == "__main__":
    process()
