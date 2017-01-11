gmail-graphite
===========
![Travis Status](https://api.travis-ci.org/jknoll/gmail-graphite.svg?branch=master)
Make sure the com.justinknoll.graphite.fullcount.plist file is owned by you and chmod 600.

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
