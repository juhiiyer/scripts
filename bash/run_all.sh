#!/usr/bin/bash

echo "today is" `date`

echo -e "\nenter the path to the directory: "
read the_path 

echo -e "\nyou path has the following files and folders: "
ls $the_path
