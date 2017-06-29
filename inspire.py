#!/usr/bin/env python3

import requests
import time
import sys

def inspire():

	# define HTTP headers

	headerDict = {
		"User-Agent" : "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" 
	}

	resultURL = requests.get("http://inspirobot.me/api?generate=true",stream=False,headers=headerDict).text+"\n"

	return resultURL

print(inspire())