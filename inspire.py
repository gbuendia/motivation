#!/usr/bin/env python3

import requests
import time
import sys

if __name__ == "__main__":

    # define HTTP headers
    # tricks API into allowing foreign GET requests
    # APIs aren't very smart
    headerDict = {
        "User-Agent" : "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" 
    }

    if len(sys.argv[1:]) > 1:
        listfile = open(str(sys.argv[1]),"w")
        for iterate in range(int(sys.argv[2])):
            time.sleep(0.3)
            resultURL = requests.get("http://inspirobot.me/api?generate=true",stream=False,headers=headerDict).text+"\n"
            sys.stdout.write(resultURL)
            listfile.write(resultURL)

        listfile.close()
        print("Done!")
    else:
        print("Not enough arguments, retard: Usage ./inspire.py output.txt 25")
