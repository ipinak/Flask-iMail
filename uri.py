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
    def get_domain():
        if kwargs is not None:
            domain = kwargs.get("domain", None)
            if domain is None:
                raise DomainNotSetError()
            return domain
        raise DomainNotSetError()

    def base_domain():
        return base_uri + get_domain()

    def messages():
        return base_domain() + "/messages"

    def domains():
        return base_uri + "domains"

    def specific_domain():
        return domains() + "/" + get_domain()

    def total_stats_uri():
        return base_domain() + "/stats/total"

    def stats_uri():
        return base_domain() + "/stats"

    def tags():
        return base_domain() + "/tags"

    def specific_tag():
        if kwargs is not None:
            tag = kwargs.get("tag", None)
            if tag is None:
                raise ArgNotSetError("tag")
            return tags() + "/" + tag
        return None

    def tag_stats():
        if kwargs is not None:
            tag = kwargs.get("tag", None)
            if tag is None:
                raise ArgNotSetError("tag")
            return tags() + "/" + tag + "/stats"
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
    if uri_type == "tags":
        return tags()
    if uri_type == "tag":
        return specific_tag()
    if uri_type == "tag.stats":
        return tag_stats()
    raise ValueError("*** Unknown type")


class DomainNotSetError(ValueError):

    def __init__(self):
        ValueError.__init__(self, "*** You must set the <domain> for Mailgun API")

class ArgNotSetError(ValueError):

    def __init__(self, error_value):
        ValueError.__init__(self, "*** You must set {0}" % (error_value))

if __name__ == '__main__':
    print(build_uri("messages", domain="ipinak.gr"))

