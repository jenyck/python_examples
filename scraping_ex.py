#!/usr/bin/env python3

from urllib.request import urlopen
html = urlopen("https://pythonscraping.com/pages/page1.html")
print(html.read())
