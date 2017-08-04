import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

m = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')
#for tag in tags:
y = (re.findall('[0-9]+',str(tags)))
y = list(map(int, y))   
 
for i in y:
    m = i + m
    
print(m)