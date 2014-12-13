# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Filename: tests.py
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Maintainer: 
# Created: Mon Sep 29 19:07:30 2014 (+0200)
# Version: 
# Last-Updated: 
#           By: 
#     Update #: 0
# Description: 
# *******************************************************************
# Keywords: 
# *******************************************************************

import unittest

# If you have not installed flask it will not run the MailGun-Flask
# integration tests
try:
    from flask import Flask
    FLASK_AVAILABLE = True
except ImportError as e:
    FLASK_AVAILABLE = False

from uri import build_uri
from mailgun_api import Mailgun

class MailgunApi_tests(unittest.TestCase):
    
    def test_MessagesURI_1(self):
        uri = build_uri("messages", domain="ipinak.gr")
        expected_uri = "https://api.mailgun.net/v2/ipinak.gr/messages"

        assert uri == expected_uri

    def test_MessagesURI_2(self):
        try:
            build_uri("messages")
        except ValueError as e:
            print("Result :> ValueError was raised as expected!")
            assert e.message == "*** You must set the <domain> for the mailgun API"

    def test_DomainsURI(self):
        uri = build_uri("domains")
        expected_uri = "https://api.mailgun.net/v2/domains"

        assert uri == expected_uri

    def test_MailingLists(self):
        uri = build_uri("mailists")
        expected_uri = "https://api.mailgun.net/v2/lists"

        assert uri == expected_uri

    def test_Specific_domain(self):
        uri = build_uri("domains.domain", domain="ipinak.gr")
        expected_uri = "https://api.mailgun.net/v2/domains/ipinak.gr"

        assert uri == expected_uri


class FlaskMailgun_test(unittest.TestCase):

    def setUp(self):
        self.app = Flask('test_flask_mailgun')
        self.mailgun = Mailgun()
        self.app.config['MAILGUN_KEY'] = 'your-key'
        self.app.config['DOMAIN'] = 'your-domain'
        self.mailgun.init_app(self.app)

    def tearDown(self):
        del self.app
        del self.mailgun

    @unittest.skipUnless(FLASK_AVAILABLE, 'It requires flask')
    def test_send_email(self):
        result = self.mailgun.send_email(
            'sender@gmail.com',
            'receiver@gmail.com',
            message='testing Flask-iMail python library',
            subject='testing Flask-iMail python library'
        )

        if result is None:
            raise Exception('wrong result back...')


if __name__ == '__main__':
    unittest.main()
