#!/usr/bin/env python
#encoding:utf8

import paramiko
import os

hostname = 'HPC ServerIP'
username = 'SSH USERNAME'

key_file = 'SSH Key PATH' #私钥文件
key_file_pwd = ''  #私钥密码


paramiko.util.log_to_file('ssh_key-login.log')
privatekey = os.path.expanduser(key_file) #私钥文件
try:
    key = paramiko.RSAKey.from_private_key_file(privatekey)
except paramiko.PasswordRequiredException:
    #需要密钥口令
    key = paramiko.RSAKey.from_private_key_file(privatekey,key_file_pwd)

ssh = paramiko.SSHClient()
ssh.load_system_host_keys(filename='/root/.ssh/known_hosts')
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,username=username,pkey=key)
stdin,stdout,stderr=ssh.exec_command('command u want') #执行远程主机系统命令
print stdout.read()
ssh.close()
