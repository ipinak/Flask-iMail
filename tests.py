# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: ipinak
# Version: 0.1
# Description:
# Keywords: tests, mailgun
# *******************************************************************
#
import unittest

# If you have not installed flask it will not run the MailGun-Flask
# integration tests
try:
    from flask import Flask
    FLASK_AVAILABLE = True
except ImportError as e:
    FLASK_AVAILABLE = False

from flask.ext.mailgun import build_uri, DomainNotSetError
from flask.ext.mailgun import Mailgun

class MailgunApi_tests(unittest.TestCase):

    BASE_URI = "https://api.mailgun.net/v2/"
    
    def test_MessagesURI_1(self):
        uri = build_uri("messages", domain="ipinak.gr")
        expected_uri = self.BASE_URI + "ipinak.gr/messages"

        assert uri == expected_uri

    def test_MessagesURI_2(self):
        try:
            build_uri("messages")
        except DomainNotSetError as e:
            print("Result :> ValueError was raised as expected!")
            assert e.message == "*** You must set the <domain> for Mailgun API"

    def test_DomainsURI(self):
        uri = build_uri("domains")
        expected_uri = self.BASE_URI + "domains"

        assert uri == expected_uri

    def test_MailingLists(self):
        uri = build_uri("mailists")
        expected_uri = self.BASE_URI + "lists"

        assert uri == expected_uri

    def test_Specific_domain(self):
        uri = build_uri("domains.domain", domain="ipinak.gr")
        expected_uri = self.BASE_URI + "domains/ipinak.gr"

        assert uri == expected_uri

    def test_TotalStats(self):
        uri = build_uri("total.stats", domain="ipinak.gr")
        expected_uri = self.BASE_URI + "ipinak.gr/stats/total"

        assert uri == expected_uri

    def test_Stats(self):
        uri = build_uri("stats", domain="ipinak.gr")
        expected_uri = self.BASE_URI + "ipinak.gr/stats"

        assert uri == expected_uri

    def test_tags(self):
        uri = build_uri("tags", domain="ipinak.gr")
        expected_uri = self.BASE_URI + "ipinak.gr/tags"

        assert uri == expected_uri

    def test_tag(self):
        uri = build_uri("tag", domain="ipinak.gr", tag="tester")
        expected_uri = self.BASE_URI + "ipinak.gr/tags/tester"

        assert uri == expected_uri

    def test_tag_stats(self):
        uri = build_uri("tag.stats", domain="ipinak.gr", tag="tester")
        expected_uri = self.BASE_URI + "ipinak.gr/tags/tester/stats"

        assert uri == expected_uri


class FlaskMailgun_test(unittest.TestCase):

    def setUp(self):
        print("\n***********************************************************************\n")
        print("If you want to run this test, you must specify a KEY and a DOMAIN above")
        print("\n***********************************************************************\n")
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
    print("***\nIf you want to run this test, you must specify a KEY and a DOMAIN above\n***")
    unittest.main()
