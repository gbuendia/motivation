#!/usr/bin/env python3

# URL request as per https://gist.github.com/mypetbirdrules/8de27e026d8c793c80d5b5557087858d
# GUI as learnt from http://usingpython.com/using-tkinter/

import tkinter
import requests
import time
import sys
# Image display as per https://www.daniweb.com/programming/software-development/code/493005/display-an-image-from-the-web-tkinter
import io
# Apparently PIL doesn't work in Python3
# so pillow has to be installed first
from PIL import Image, ImageTk

# Headers for the requests we make, otherwise we'll get error 403
headerDict = {
		"User-Agent" : "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19" 
	}

def inspire():
	resultURL = requests.get("http://inspirobot.me/api?generate=true",stream=False,headers=headerDict).text
	return resultURL

def getimage(url):
	picdata = requests.get(url,headers=headerDict)
	# Create an image file object
	picture = io.BytesIO(picdata.content)
	# Use PIL to read formats like jpg, png...
	picture_pil = Image.open(picture)
	# Convert to an image that TKinter can handle
	tk_picture = ImageTk.PhotoImage(picture_pil)
	return tk_picture

def updateimage():
	another_motivational = getimage(inspire())
	poster.configure(image = another_motivational)
	# Not sure what the garbage collection does:
	# https://stackoverflow.com/questions/3482081/how-to-update-the-image-of-a-tkinter-label-widget
	poster.image = another_motivational
	# Let 3 secs pass to not abuse the server
	temp_btn_disable(3)

def quit():
	global root
	root.destroy()

def temp_btn_disable(seconds):
	poster.configure(state = "disabled")
	time.sleep(seconds)
	poster.configure(state = "normal")

# Create new window
root = tkinter.Tk()
# Decorate window
root.title("Inspire")
root.geometry("650x682") # Apparently all images returned by InspireBot are this 650x650
root.wm_iconbitmap("lightbulb.ico")

# Put the image on the window for first time
# Get the image
motivational = getimage(inspire())
# Put the image on a typical widget
poster = tkinter.Label(root, image = motivational)
# Pack (add) it into window
poster.pack()

# Create the button, to be used to refresh
# fg and bg change text and background colors but macos does not support that
btn_refresh = tkinter.Button(text="More inspiration",fg="white",bg="black",command=updateimage)
# Pack the button, filling the width
btn_refresh.pack(side="left",expand=True)

# Create the button to quit
btn_quit = tkinter.Button(text="Quit",fg="white",bg="black",command=quit)
btn_quit.pack(side="right",expand=True)

# Draw the window, start app
root.mainloop()