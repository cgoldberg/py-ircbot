#! /usr/bin/env python
#
#  ircbot - simple IRC bot in Python
#  -----------------------------------
#  * https://github.com/cgoldberg/ircbot
#  * Corey Goldberg <cgoldberg@gmail.com>, 2013
#
#  license:
#  --------
#  * GNU GPLv3
#
#  requirements:
#  -------------
#  * Python 2.7+/3.2+
#  * `irc` package
#    * PyPI (install): https://pypi.python.org/pypi/irc
#    * BitBucket (dev): https://bitbucket.org/jaraco/irc


"""Simple IRC bot using `irc` package.

This bot uses the `SingleServerIRCBot` class from the `irc.bot` module.
The bot enters a channel and listens for commands in private messages
and channel traffic. Commands in channel messages are given by prefixing
the text by the bot name followed by a colon.

The known commands are:

    stats -- Print channel information.
    die -- Let the bot cease to exist.

"""


import irc.bot
import irc.strings


class TestBot(irc.bot.SingleServerIRCBot):
    def __init__(self, server, port, channel, nickname):
        irc.bot.SingleServerIRCBot.__init__(
            self, [(server, port)], nickname, nickname
        )
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + '_')

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        a = e.arguments[0].split(':', 1)
        if len(a) > 1 and \
        irc.strings.lower(a[0]) == \
        irc.strings.lower(self.connection.get_nickname()):
            self.do_command(e, a[1].strip())
        return

    def on_dccmsg(self, c, e):
        c.privmsg('You said: ' + e.arguments[0])

    def do_command(self, e, cmd):
        nick = e.source.nick
        c = self.connection

        if cmd == 'die':
            self.die()
        elif cmd == 'stats':
            for chname, chobj in self.channels.items():
                c.notice(nick, '--- Channel statistics ---')
                c.notice(nick, 'Channel: ' + chname)
                users = chobj.users()
                users.sort()
                c.notice(nick, 'Users: ' + ', '.join(users))
                opers = chobj.opers()
                opers.sort()
                c.notice(nick, 'Opers: ' + ', '.join(opers))
                voiced = chobj.voiced()
                voiced.sort()
                c.notice(nick, 'Voiced: ' + ', '.join(voiced))
        else:
            c.notice(nick, 'Command Not Understood: ' + cmd)


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('server', help='irc server name')
    parser.add_argument('port', type=int, help='irc server port')
    parser.add_argument('channel', help='channel name')
    parser.add_argument('nickname', help='user name')
    args = parser.parse_args()

    if args.channel.startswith('#'):
        channel = args.channel
    else:
        channel = '#' + args.channel

    bot = TestBot(args.server, args.port, channel, args.nickname)
    try:
        bot.start()
    except KeyboardInterrupt:
        print('\nInterrupted')
