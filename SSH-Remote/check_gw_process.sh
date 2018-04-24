#!/bin/bash

function lsofcount(){
    processid=$(sudo ps uf |grep $1|awk '{print $2}')

    count=$(sudo lsof -p $processid|wc -l)

    echo ${count}
}

lsofcount $1

