#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6614216476:AAFDybAx7C27HAjo2AVPWiwxwwM_i2RMzvk")
    API_ID = int(os.environ.get("API_ID", "27039595"))
    API_HASH = os.environ.get("API_HASH", "aabe9b61bbdb73ea4b35fc4faa880621")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6387516803")
