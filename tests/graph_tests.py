from nose.tools import *
import gmail_graphite.graph

def setup():
  print "Setup"

def teardown():
  print "Tear down"

def test_basic():
  gmail_graphite.graph.process()
