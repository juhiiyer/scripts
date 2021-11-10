#!/bin/bash

file_name=$1
awk '/STAR/ {print $2}' $file_name |awk -F: '{print $1}' >star.txt
awk '/GUI/ {print $2}' $file_name  |awk -F: '{print $1}'>gui.txt
echo 'ig its done'
