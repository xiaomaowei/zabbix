#!/usr/bin/env bash
# 先获取nfs server ip，然后从ip去grep mount -l，获得mount volume

nfsarray=(`cat /proc/net/nfsfs/servers | sed -n '2,$p' | awk '{print $5}'|sort|uniq   2>/dev/null`)
length=${#nfsarray[@]}
printf "{\n"
printf  '\t'"\"data\":["
for ((i=0;i<$length;i++))
do
        volume=`mount -l |grep ${nfsarray[$i]} |awk '{print $3}'`
        printf '\n\t\t{'
        printf "\"{#NFSVOLUME}\":\"$volume\"}"
        if [ $i -lt $[$length-1] ];then
                printf ','
        fi
done
printf  "\n\t]\n"
printf "}\n"