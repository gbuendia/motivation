#!/usr/bin/env python3

# URL request as per https://gist.github.com/mypetbirdrules/8de27e026d8c793c80d5b5557087858d
# GUI as learnt from http://usingpython.com/using-tkinter/

import tkinter
import requests
import time
import sys
# Image display as per https://www.daniweb.com/programming/software-development/code/493005/display-an-image-from-the-web-tkinter
import io
from urllib.request import Request, urlopen
# Apparently PIL doesn't work in Python3
# so pillow has to be installed first
from PIL import Image, ImageTk

def inspire():
	# define HTTP headers
	headerDict = {
		"User-Agent" : "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" 
	}
	resultURL = requests.get("http://inspirobot.me/api?generate=true",stream=False,headers=headerDict).text
	return resultURL

def getimage(url):
	headerDict = {
		"User-Agent" : "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" 
	}
	picdata = requests.get(url,headers=headerDict)
	# Create an image file object
	picture = io.BytesIO(picdata.content)
	# Use PIL to read formats like jpg, png...
	picture_pil = Image.open(picture)
	return picture_pil

# Create new window
window = tkinter.Tk()
# Decorate window
window.title("Inspire")
window.geometry("650x650") # Apparently all images returned by InspireBot are this size
window.wm_iconbitmap('lightbulb.ico')

# Get the image
motivational = getimage(inspire())
# Convert to an image that TKinter can handle
tk_picture = ImageTk.PhotoImage(motivational)
# Put the image on a typical widget
label = tkinter.Label(window, image = tk_picture)
# Pack (add) it into window
label.pack(padx=0, pady=0)

# Draw the window, start app
window.mainloop()