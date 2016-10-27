gmail-graphite
===========

To start the launchctl service:
    $ ./start.sh

Test w/ this command:

    $ launchctl list | grep graphite

It should output something like:

    $ launchctl list | grep graphite
    -				0	com.justinknoll.graphite.fullcount

Copy the script to ~/bin:

    $ cp inbox_feed_graphite.py ~/bin/

Edit credentials including your hosted graphite API key.

Install feedparser

    $ sudo easy_install feedparser

Note: this mechanism is incompatible with two-factor authentication.