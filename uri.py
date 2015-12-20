# !/usr/bin/env python
# -*- coding:utf-8 -*-
# *******************************************************************
# Author: Ioannis Pinakoulakis
# Version: 0.1
# Description:
# Keywords: URI, mailgun
# *******************************************************************
#

DEFAULT_MAILGUN_URI="https://api.mailgun.net/v2/"

def build_uri(uri_type, base_uri=DEFAULT_MAILGUN_URI, **kwargs):
    """
    :param base_uri
    :param uri_type
    :param kwargs
    :return - the URI in string format
    """
    def messages():
        if kwargs is not None:
            domain = kwargs.get("domain")
            if domain is None:
                raise ValueError("*** You must set the <domain> for the mailgun API")
        return base_uri + domain + "/messages"

    def specific_domain():
        if kwargs is not None:
            domain = "/" + kwargs.get("domain")
            if domain is None:
                raise ValueError("*** You must set the <domain> for the mailgun API")
        return domains() + domain

    if uri_type == "messages":
        return messages()
    if uri_type == "mailists":
        return base_uri + "lists"
    if uri_type == "domains":
        return base_uri + "domains"
    if uri_type == "domains.domain":
        return specific_domain()
    if uri_type == "address.validate":
        return base_uri + "address/validate"
    raise ValueError("*** Unknown type")


if __name__ == '__main__':
    print build_uri("messages", domain="ipinak.gr")
