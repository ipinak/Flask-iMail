# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: ipinak
# Version: 0.1
# Description:
# Keywords: mailgun, email
# *******************************************************************
#
__author__ = 'ipinak'

import requests
import uri as _u
import utils

# Export
build_uri = _u.build_uri
DomainNotSetError = _u.DomainNotSetError

class Mailgun(object):

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        self.mailgunApi = MailgunApi(app.config.get('MAILGUN_KEY'),
                                     app.config.get('DOMAIN'))
        self.app = app

    def send_email(self, sender, receiver, message, **kwargs):
        return self.mailgunApi.send_email(sender, receiver,
                                          message=message,
                                          **kwargs
        )


class _YARequest(object):
    '''_YARequest - Yet Another Request'''

    def __init__(self, auth=None):
        self._auth = auth

    @property
    def auth(self):
        return self._auth

    def get(self, uri, data):
        return requests.get(uri, auth=self.auth, data=data)

    def post(self, uri, data):
        return requests.post(uri, auth=self.auth, data=data)

    def delete(self, data):
        return requests.delete(uri, auth=self.auth, data=data)

    def put(self, data):
        return requests.put(uri, auth=self.auth, data=data)


class MailgunApi(_YARequest):

    def __init__(self, api_key, domain):
        _YARequest.__init__(self, ('api', api_key))
        self.domain = domain

    def send_email(self, sender, receiver, **kwargs):
        """
        :param sender
        :param receiver
        :param message
        :param kwargs - subject, attachments
        :return - result from mailgun
        """
        if kwargs is not None:
            subject = kwargs.get('subject') or "Unknown subject"
            message = kwargs.get('message')
            html = kwargs.get('html')
            if html is not None:
                data = {"from": sender,
                        "to": receiver,
                        "subject": subject,
                        "html": html}
            else:
                data = {"from": sender,
                        "to": receiver,
                        "subject": subject,
                        "text": message}

            if kwargs.has_key('attachments'):
                data['files'] = kwargs['attachments']

        response = self.post(_u.build_uri("messages", domain=self.domain), data)
        return utils.handle_response(response)

    def get_domains(self):
        """
        :return: a dictionary with the data from the response
        """
        response = self.get(_u.build_uri("domains"), data=None)
        return utils.handle_response(response)

    def validate_email(self, email):
        """
        Validate an email using Mailgun.
        :param email: the email in string format.
        :return: a dictionary with the data from the response
        """
        data = {
            "address": email
        }
        resp = self.get(_u.build_uri("address.validate"), data)
        return utils.handle_response(resp)

    def get_total_stats(self, **kwargs):
        """
        Get the total stats of a specified domain (`<domain/stats/total`).
        :param kwargs: parameters to query the service:
            `event`, `start`, `end`, `resolution`, `duration`
        :return: a dictionary with data from the response
        """
        resp = self.get(_u.build_uri("total.stats", domain=self.domain), kwargs)
        return utils.handle_response(resp)

    def get_stats(self, **kwargs):
        """
        Returns a list of event stats items. Each record represents counts for one event per one day.
        :params kwargs: parameters to query the service: `limit`, `skip`, `event`, `start-date`
        :return: a dictionary with the data from the response
        """
        resp = self.get(_u.build_uri("stats"), kwargs)
        return utils.handle_response(resp)


if __name__ == "__main__":
    mGun = MailgunApi(api_key="you-key",
                      domain="ipinak.gr"
    )
    mGun.send_email(sender="ipinak@sample-domain.com",
                    receiver="email@sample-domain.com",
                    message="Testing the MailgunApi that I have written...",
                    subject="test subject"
    )
