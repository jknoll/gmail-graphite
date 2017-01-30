#!/usr/bin/env python
import feedparser
import socket
from config import config
from pickle import dumps, dump


def dump_feed_response(url):
    # Useful for dumping the response for use in mocking during testing.
    d = feedparser.parse(url)
    f = file('tests/feedoutput.pickle', 'w+')
    dump(d, f)


def get_count(url):
    d = feedparser.parse(url)
    try:
        return d['feed']['fullcount']
    except KeyError as e:
        print "KeyError: %s" % str(e)


def send_count(count):
    message = config['graphite_prefix'] + " %s\n" % count
    conn = socket.create_connection((config['graphite_host'],
                                     config['graphite_port']))
    conn.send(message)
    conn.close()


def process():
    count = get_count(config['gmail_feed_url'])
    send_count(count)

if __name__ == "__main__":
    process()
