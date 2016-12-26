from nose.tools import *
import gmail_graphite.graph as graph
from config import config

def setup():
  print "Setup"

def teardown():
  print "Tear down"

def test_get_count():
  count = graph.get_count(config['gmail_feed_url'])
  assert_greater_equal(count, 0)

def test_basic():
  graph.process()
