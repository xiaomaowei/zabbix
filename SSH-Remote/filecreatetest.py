#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import sys
import signal


# 定义一个信号处理函数，该函数打印收到的信号，然后raise IOError
def handler(signum, frame):
    print 'Signal handler called with signal', signum
    raise IOError("Couldn't open device!")


# 对SIGALRM(终止)设置处理的handler, 然后设置定时器，5秒后触发SIGALRM信号
signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

try:
    # This open() may hang indefinitely
    f = open('/' + sys.argv[1] + 'testfile.txt', "w+")
    f.write("ok")
    f.seek(os.SEEK_SET)
    context = f.read()
    f.close()
    os.remove('/' + sys.argv[1] + 'testfile.txt')
    print "1"
except:
    print("0")

signal.alarm(0)  # 关闭定时器