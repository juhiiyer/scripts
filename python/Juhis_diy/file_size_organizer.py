#!/usr/bin/env python3

import shutil

path = input('Please enter file path: ')
memory = shutil.disk_usage(path)

print(memory[:'free'])
