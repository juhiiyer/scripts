#!/bin/bash

file_name=$1
if [[ $# -ne 1 ]]
   then
     echo "need exactly one argument"
     exit 1
fi

if [[ ! -f $# ]]; then
    echo "file doesnt exist."
    exit 1
fi

awk '/STAR/ {print $2}' $file_name |awk -F: '{print $1}' >star.txt
awk '/GUI/ {print $2}' $file_name  |awk -F: '{print $1}'>gui.txt
echo 'ig its done'
