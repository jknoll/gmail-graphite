gmail-graphite
===========
To enable the launchd action:
launchctl load ~/Documents/git/gmail-graphite/com.justinknoll.graphite.fullcount.plist
launchctl start com.justinknoll.graphite.fullcount

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
