#!/bin/bash

function lsofcount(){
    gwpath='/home/lambda/lambdacal/gw_server/bin/'
    processid=$(sudo ps aux |grep "${gwpath}$1"|grep "$2"|awk '{print $2}'|tail -1)

    count=$(sudo lsof -p $processid|wc -l)

    echo ${count}
}

lsofcount $1