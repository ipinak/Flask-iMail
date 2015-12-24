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
            domain = kwargs.get("domain", None)
            if domain is None:
                raise DomainNotSetError()
        return base_uri + domain + "/messages"

    def domains():
        return base_uri + "domains"

    def specific_domain():
        if kwargs is not None:
            domain = "/" + kwargs.get("domain", None)
            if domain is None:
                raise DomainNotSetError()
            return domains() + domain
        return None

    def total_stats_uri():
        if kwargs is not None:
            domain = kwargs.get("domain", None)
            if domain is None:
                raise DomainNotSetError()
            return base_uri + domain + "/stats/total"
        return None

    def stats_uri():
        if kwargs is not None:
            domain = kwargs.get("domain", None)
            if domain is None:
                raise DomainNotSetError()
            return base_uri + domain + "/stats"
        return None

    if uri_type == "messages":
        return messages()
    if uri_type == "mailists":
        return base_uri + "lists"
    if uri_type == "domains":
        return domains()
    if uri_type == "domains.domain":
        return specific_domain()
    if uri_type == "address.validate":
        return base_uri + "address/validate"
    if uri_type == "total.stats":
        return total_stats_uri()
    if uri_type == "stats":
        return stats_uri()
    raise ValueError("*** Unknown type")


class DomainNotSetError(ValueError):

    def __init__(self):
        ValueError.__init__(self, "*** You must set the <domain> for Mailgun API")

if __name__ == '__main__':
    print(build_uri("messages", domain="ipinak.gr"))

