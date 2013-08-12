py-ircbot
=========

simple IRC bot in Python
------------------------

* https://github.com/cgoldberg/py-ircbot
* Corey Goldberg, <cgoldberg@gmail.com>, 2013

license:
--------

* GNU GPLv3

requirements:
-------------

* Python 2.7+/3.2+
* `irc` package:

 * PyPI: https://pypi.python.org/pypi/irc
 * Development: https://bitbucket.org/jaraco/irc

* `mock` package (for testing only):

 * PyPI: https://pypi.python.org/pypi/mock
 * Development: http://www.voidspace.org.uk/python/mock

Usage:
------

`ircbot.py` is invoked with the following 4 positional arguments:

 * server
 * port
 * channel
 * nickname

for example: to join the `#python` channel on Freenode using the nickname "mybot" ::

    $ python ircbot.py irc.freenode.net 8000 python mybot

Note: you don't need to prepend a "#" to the channel name.  If you do, you
must either escape the character or put the entire argument in quotes:: 

    $ python ircbot.py irc.freenode.net 8000 \#python mybot
    $ python ircbot.py irc.freenode.net 8000 "#python" mybot

