#!/usr/bin/python3
import requests

''' its chewy ur gurl coming back wether to find out
if ur website is truly pingable or not
stay tuned to get this free test
'''
global WEBSITE



WEBSITE = ''
WEBSITE = input('please print ur website including http or https: ')

print('u entered the url %s' % WEBSITE)

def add_http(url):
			
		print('You forgot to add http:// to your input you donut I will do it for you.')
		global WEBSITE

		WEBSITE = 'http://' + url
		# print('the value of WEBSITE is {}'.format(WEBSITE))
		 

def url_ok(WEBSITE):
    ping_result = requests.head(WEBSITE)

    if ping_result.status_code == 200:
        print('pinged succecfuly.')
    else:
        print('not pingable')

if 'http://' not in (WEBSITE):
	add_http(WEBSITE)

# print('the value of WEBSITE is {}'.format(WEBSITE))

url_ok(WEBSITE)
