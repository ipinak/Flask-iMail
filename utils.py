#!/bin/env python
# -*- coding:utf-8 -*-
# ***********************************************************************
# Author: ipinak
# Description:
# Version: 0.1
# Keywords: mailgun, utils, response
# ***********************************************************************
#
__author__ = 'ipinak'

import json

def handle_response(response):
    if response.status_code == 200:
        return json.loads(response.content)
    return None