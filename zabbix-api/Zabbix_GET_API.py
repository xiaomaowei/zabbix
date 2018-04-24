#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Denis
# 2018/04/24

import sys
from pyzabbix import ZabbixAPI

zapi = ZabbixAPI("http://zabbix:port")
zapi.login('user', 'pw')

name = sys.argv[1]

jobid = name.split(':')[1]

result = zapi.item.get(
	search={"key_": jobid}
)

for items in result:
	zapi.item.update(
		itemid=items['itemid'],
		status=1
	)
