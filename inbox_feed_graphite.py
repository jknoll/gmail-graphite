#!/usr/bin/env python
import feedparser
import socket

d = feedparser.parse('https://username@example.org:password@gmail.google.com/mail/feed/atom')
fullcount = d['feed']['fullcount']

message = "api_key.personal.email.bittorrent.fullcount %s\n" % fullcount

conn = socket.create_connection(("carbon.hostedgraphite.com", 2003))
conn.send(message)
conn.close()
