#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Denis
# 2018/04/20

import sys
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://zabbix ip:port")
zapi.login("username", "password")

jobs = zapi.item.update(
    itemid=sys.argv[1],
    status="0"
)
