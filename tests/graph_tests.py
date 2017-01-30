from nose.tools import *
import feedparser
from pickle import load
from mock import MagicMock
from pprint import pprint
from subprocess import call, CalledProcessError
from config import config

feedoutput = ''


def setup():
    print "Setup"
    f = open('tests/feedoutput.pickle', 'r')
    global feedoutput
    feedoutput = load(f)
    try:
        call(["cp", "config.py", "config_backup.py"])
        call(["cp", "tests/config.py", "config.py"])
        # Need this import below the config-generation above
        global graph
        import gmail_graphite.graph as graph
    except CalledProcessError as e:
        print e.output


def teardown():
    print "Tear down"
    call(["mv", "config_backup.py", "config.py"])


def test_get_count():
    setup()
    feedparser.parse = MagicMock(return_value=feedoutput)
    graph.send_count = MagicMock(return_value=True)
    count = graph.get_count(config['gmail_feed_url'])
    assert_greater_equal(count, 0)
    teardown()


def test_basic():
    graph.process()
