#!/bin/python

import urllib.request
import os

# find url

url = "https://bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=fi-FI"

contents = str(urllib.request.urlopen(url).read())

url = "https://bing.com/" + contents.split("<url>")[1].split("</url>")[0]

# download

img = urllib.request.urlopen(url).read()
with open('/home/jakes/bgChanger/image.jpg', 'wb') as handler:
    handler.write(img)

# make sure the bg is set

os.system("feh --bg-scale /home/jakes/bgChanger/image.jpg")
