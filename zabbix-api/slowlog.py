#!/bin/python
# -*- coding: utf-8 -*-

import json
from pyzabbix import ZabbixAPI
from datetime import datetime
from src.QcloudApi.qcloudapi import QcloudApi

zapi = ZabbixAPI("http://zabbix ip:port")
zapi.login("username", "password")

module = 'cdb'
action = 'DescribeCdbSlowQueryLog'
config = {
    'Region': 'sh',
    'secretId': '',
    'secretKey': '',
    'method': 'post'
}
params = {
    'cdbInstanceId': 'cdb-l1w9eda6',
    'limit': '100'
}
try:
    service = QcloudApi(module, config)
    # print service.generateUrl(action, params)

    with open('/usr/local/zabbix/frontends/php/slowlog/' + datetime.now().date().strftime('%Y.%m.%d') + '_slowquery.txt', 'w') as f:

        # print service.call(action, params)
        print >> f, service.call(action, params)

        result = json.loads(service.call(action, params))
        querycount = result["totalCount"]+21

        triggers = zapi.trigger.update(
        triggerid='15956',
        description="{master_001:mysql.status[Slow_queries].last()}>" + str(querycount),
        expression="{master_001:mysql.status[Slow_queries].last()}>" + str(querycount)
        )

except Exception, e: