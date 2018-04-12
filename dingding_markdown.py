#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Denis
# 2018/04/12

import requests
import json
import sys
import os
import time
import configparser

headers = {'Content-Type': 'application/json;charset=utf-8'}
time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

config=configparser.ConfigParser()
config.read('/usr/local/zabbix/conf/dingding.conf')

log_file = config.get('config','log')
api_url = config.get('config','webhook')


def log(info):
    if os.path.isfile(log_file) == False:
               f = open(log_file, 'a+')

    f = open(log_file,'a+')
    f.write(info)
    f.close()

#for text style use
#def msg(text,user):
#    json_text= {
#     "msgtype": "text",
#        "text": {
#            "content": text
#        },
#        "at": {
#            "atMobiles": [
#                user
#            ],
#            "isAtAll": False
#        }
#    }

def msg(text,user,title):
    json_text= {
        "msgtype": "markdown",
        "markdown": {
                "title": title,
                "text": text + "\n ###### @" + user
         },
        "at": {
            "atMobiles": [
                user
            ],
            "isAtAll": False
        }
    }

    r=requests.post(api_url,data=json.dumps(json_text),headers=headers).json()
    code = r["errcode"]
    if code == 0:
        log(time + ":Message Send Success Return Code:" + str(code) + "\n")
    else:
        log(time + ":Message Send False Return Code:" + str(code) + "\n")
        exit(3)

if __name__ == '__main__':
    text = sys.argv[1]
    user = sys.argv[2]
    title = sys.argv[3]
    msg(text,user,title)
