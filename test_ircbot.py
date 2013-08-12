#!/usr/bin/env python
#
#   This file is part of py-ircbot
#
#   Corey Goldberg, 2013
#   License: GPLv3


"""Unit tests for ircbot"""


import unittest

import mock
import irc

import ircbot


class IrcLibTestCase(unittest.TestCase):

    def test_version(self):
        self.assertTrue(hasattr(irc.client, 'VERSION'))
        self.assertIsInstance(irc.client.VERSION, tuple)
        self.assertGreaterEqual(irc.client.VERSION, (8, 0))

    def test_construct_bot(self):
        bot = irc.bot.SingleServerIRCBot(
            server_list=[('localhost', '6667')],
            realname='py-ircbot',
            nickname='ircbot',
        )
        self.assertEqual(len(bot.server_list), 1)
        svr = bot.server_list[0]
        self.assertEqual(svr.host, 'localhost')
        self.assertEqual(svr.port, '6667')
        self.assertIsNone(svr.password)

    @mock.patch('irc.connection.socket')
    def test_privmsg_sends_msg(self, socket_mod):
        server = irc.client.IRC().server()
        server.connect('test_server', 6667, 'my_nickname')
        # make sure the mock object doesn't have a write method or it will
        # treat it as an SSL connection and never call .send.
        del server.socket.write
        server.privmsg('#best-channel', 'You are great')
        server.socket.send.assert_called_with(
            b'PRIVMSG #best-channel :You are great\r\n')


class IrcBotTestCase(unittest.TestCase):
    #TODO: write tests!
    pass


if __name__ == '__main__':
    unittest.main()
