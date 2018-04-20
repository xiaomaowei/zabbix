#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Denis
# 2018/04/19

from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://zabbix ip:port")
zapi.login("username", "password")
# print("Connected to Zabbix API Version %s" % zapi.api_version())

triggers = zapi.trigger.update(
    triggerid='triggerid',
    expression="trigger expressions"
)

print triggers
