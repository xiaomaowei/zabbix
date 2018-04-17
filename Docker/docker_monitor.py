#!/usr/bin/env python
import docker
import sys
import subprocess
import os
import json
def check_container_stats(container_name,collect_item):
    #docker_client = docker_client.containers.get(container_name)
    global result
    container_collect=docker_client.containers.get(container_name).stats(stream=True)
    old_result=json.loads(container_collect.next())
    new_result=json.loads(container_collect.next())
    container_collect.close()

    if collect_item == 'cpu_total_usage':
        result=new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']

    elif collect_item == 'cpu_system_usage':
        result=(new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage'])/10 ^ 8

    elif collect_item == 'cpu_percent':
        cpu_total_usage=new_result['cpu_stats']['cpu_usage']['total_usage'] - old_result['cpu_stats']['cpu_usage']['total_usage']
        cpu_system_uasge=new_result['cpu_stats']['system_cpu_usage'] - old_result['cpu_stats']['system_cpu_usage']
        cpu_num=len(old_result['cpu_stats']['cpu_usage']['percpu_usage'])
        result=round((float(cpu_total_usage)/float(cpu_system_uasge))*cpu_num*100.0,2)

    elif collect_item == 'mem_usage':
        result=new_result['memory_stats']['usage']

    elif collect_item == 'mem_limit':
        result=new_result['memory_stats']['limit']

    elif collect_item == 'network_rx_bytes':
        result=(new_result['networks']['eth0']['rx_bytes'] - old_result['networks']['eth0']['rx_bytes'])*8

    elif collect_item == 'network_tx_bytes':
        result=(new_result['networks']['eth0']['tx_bytes'] - old_result['networks']['eth0']['tx_bytes'])*8

    elif collect_item == 'mem_percent':
        mem_usage=new_result['memory_stats']['usage']
        mem_limit=new_result['memory_stats']['limit']
        result=round(float(mem_usage)/float(mem_limit)*100.0,2)

    elif collect_item == "blk_io_read":
        r_list = new_result['blkio_stats']['io_service_bytes_recursive']
        for r_dict in r_list:
            if r_dict['major'] == 253 and r_dict['op'] == "Read" and r_dict['minor'] == 0:
                result = r_dict['value']

    elif collect_item == "blk_io_write":
        w_list = new_result['blkio_stats']['io_service_bytes_recursive']
        for w_dict in w_list:
            if w_dict['major'] == 253 and w_dict['op'] == "Write" and w_dict['minor'] == 0:
                result = w_dict['value']

    return result

if __name__ == "__main__":

    docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock', version='1.27')
    container_name=sys.argv[1]
    collect_item=sys.argv[2]
    print check_container_stats(container_name,collect_item)