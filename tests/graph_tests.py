from nose.tools import *
import gmail_graphite.graph as graph
import feedparser
from pickle import load
from mock import MagicMock
from pprint import pprint

feedoutput = ''
config = {
    'gmail_feed_url': '',
    'graphite_prefix': '',
    'graphite_host': '',
    'graphite_port': ''
}


def setup():
    print "Setup"
    f = open('tests/feedoutput.pickle', 'r')
    global feedoutput
    feedoutput = load(f)


def teardown():
    print "Tear down"


def test_get_count():
    setup()
    feedparser.parse = MagicMock(return_value=feedoutput)
    count = graph.get_count(config['gmail_feed_url'])
    assert_greater_equal(count, 0)


def test_basic():
    graph.process()
