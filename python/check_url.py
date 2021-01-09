#!/usr/bin/python3
import requests

''' its chewy ur gurl coming back wether to find out
if ur website is truly pingable or not
stay tuned to get this free test
'''

WEBSITE = input('please print ur website including http or https: ')

print('u entered the url %s' % WEBSITE)

def url_ok(url):
    ping_result = requests.head(url)

    if ping_result.status_code == 200:
        print('pinged succecfuly.')
    else:
        print('not pingable')


url_ok(WEBSITE)