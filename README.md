gmail-graphite
===========
To enable the launchd action:
launchctl load ~/Documents/python/gmail-oauth/com.justinknoll.graphite.fullcount.plist
launchctl start com.justinknoll.graphite.fullcount

Test w/ this command:

    $ launchctl list | grep graphite

It should output something like:

    $ launchctl list | grep graphite
    -				0	com.justinknoll.graphite.fullcount
