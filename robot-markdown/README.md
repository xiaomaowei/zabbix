# zabbix 钉钉机器人 markdown 版本

    取自网上的版本更改的，来源已经忘记了。。。

## 配置文件

 
 - dingding_markdown.py 脚本本体，需要更改的地方只有一个
 - config.read('/usr/local/zabbix/conf/dingding.conf') #机器人配置文件的路径
 - dingding.conf 机器人配置文件，两个需要更改的地方

	    log=/var/log/zabbix/zabbix_dingding.log #存放机器人日志的路径
	    webhook=https://oapi.dingtalk.com/robot/send?access_token=xxxx #机器人的token

## 安装方式

    cp dingding_markdown.py /usr/local/zabbix/alertscripts
    cp dingding.conf /usr/local/zabbix/conf
    chmod +x /usr/local/zabbix/conf/dingding_markdown.py
    chown zabbix:zabbix /usr/local/zabbix/conf/dingding_markdown.py

## zabbix配置

### zabbix web界面，管理 =》 报警媒介类型 =》 创建媒体类型

 - 名称：钉钉机器人
 - 脚本名称：dingding_markdown.py
 - 脚本参数：{ALERT.MESSAGE} {ALERT.SENDTO} {ALERT.SUBJECT} 3个，必须按照顺序
 
### zabbix web界面，配置 =》 动作 =》 事件源【触发器】=》 创建动作
 **- 动作**

	 - 名称：钉钉报警
 **- 操作**
	 - 默认操作步骤持续时间：1h
	 - 默认接收人:服务器：{HOST.NAME} 发生：{TRIGGER.NAME}故障
	 - 默认信息:

	    #### {TRIGGER.NAME} 发生问题
	    ###### 故障时间：{EVENT.DATE} {EVENT.TIME}
	    ###### 故障时长：{EVENT.AGE}
	    ###### 告警级别：{TRIGGER.SEVERITY}
	    ###### 故障事件ID：[{EVENT.ID}](http://这边替换掉zabbix的ip或是域名/tr_events.php?triggerid={TRIGGER.ID}&eventid={EVENT.ID})
	    ###### 故障主机IP：{HOST.IP}
	    ###### 故障主机名：{HOST.NAME}
	    ###### 故障是否确认：{EVENT.ACK.STATUS}
	    #### 当前状态：{ITEM.LASTVALUE}
	    
 - 操作：
 
	    发送消息给用户: Admin (Zabbix Administrator) 通过 钉钉机器人 立即地 默认
	    
 - **恢复操作**

	 - 默认操作步骤持续时间：1h
	 - 默认接收人:服务器：{HOST.NAME} 问题：{TRIGGER.NAME}已恢复！
	 - 默认信息:

		    #### {TRIGGER.NAME} 已经恢复
		    ###### 恢复时间：{EVENT.RECOVERY.DATE} {EVENT.RECOVERY.TIME}
		    ###### 故障时长：{EVENT.AGE}
		    ###### 当前状态：{EVENT.STATUS}
		    ###### 故障事件ID：[{EVENT.ID}](http://这边替换掉zabbix的ip或是域名/tr_events.php?triggerid={TRIGGER.ID}&eventid={EVENT.ID})
		    ###### 故障主机IP：{HOST.IP}
		    ###### 故障主机名：{HOST.NAME}
		    ###### 故障是否确认：{EVENT.ACK.STATUS}
		    #### 当前状态：{ITEM.LASTVALUE}

	 - 操作：

		    发送消息给用户: Admin (Zabbix Administrator) 通过 钉钉机器人 立即地 默认
 - **确认操作**
	 - 默认操作步骤持续时间：1h
	 - 默认接收人:服务器：{HOST.NAME} 问题：{TRIGGER.NAME}已确认！
	 - 默认信息:

		    #### 管理员{USER.FULLNAME} 已经发布故障原因
		    ###### 确认时间：{ACK.DATE} {ACK.TIME}
		    ###### 故障时长：{EVENT.AGE}
		    ###### 当前状态：{EVENT.STATUS}
		    ###### 故障主机IP：{HOST.IP}
		    ###### 故障事件ID：{EVENT.ID}
		    ###### 故障主机名：{HOST.NAME}
		    ###### 故障前状态：{ITEM.LASTVALUE}
		    ###### 故障是否确认：{EVENT.ACK.STATUS}
		    {ACK.MESSAGE}

	 - 操作：

		    发送消息给用户: Admin (Zabbix Administrator) 通过 钉钉机器人 立即地 默认

