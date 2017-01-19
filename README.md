gmail-graphite
==============

<!---
![Travis Status](https://api.travis-ci.org/jknoll/gmail-graphite.svg?branch=master)
-->

Installation
------------

To install on Mac OS El Capitan or later, you'll need to ensure you're running a user-modifiable python framework or you'll run into issues with pip install being blocked by System Integrity Protection.

Install python via homebrew:

    $ brew install python
    $ pip --version

Copy config and add credentials including your hosted graphite API key:

    $ cp config_example.py config.py

To start the launchctl service:
    $ ./start.sh

Test w/ this command:

    $ launchctl list | grep graphite

It should output something like:

    $ launchctl list | grep graphite
    -				0	com.justinknoll.graphite.fullcount

Copy the script to ~/bin:

    $ cp inbox_feed_graphite.py ~/bin/

To make the launchd scripts run as a daemon on boot, you will need to set the .plist files chown root and chmod wheel, then copy them to /Library/LaunchDaemons/.

Notes
-----

This mechanism is incompatible with two-factor authentication.

Make sure the com.justinknoll.graphite.fullcount.plist file is owned by you and chmod 600.

It appears that you cannot refer to ~ within the paths in the .plist.

If forced to modify the .plist, you can validate your edits with:

    $ plutil com.justinknoll.graphite.fullcount.plist

If running the ~/bin/ file works, but launchd seems to be failing, try:

    $ tail -f /var/log/system.log # Or use Console.app and search for launchd.
