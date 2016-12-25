try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description': 'Tracks GMail inbox unread message count via RSS and Graphite',
  'author': 'Justin Knoll',
  'url': 'https://github.com/jknoll/gmail-graphite',
  'download_url': 'https://github.com/jknoll/gmail-graphite',
  'author_email': 'justin.knoll@gmail.com',
  'version': '0.1',
  'install_requires': ['nose', 'feedparser'],
  'packages': ['gmail-graphite'],
  'scripts': [],
  'name': 'gmail-graphite'
}

setup(**config)
