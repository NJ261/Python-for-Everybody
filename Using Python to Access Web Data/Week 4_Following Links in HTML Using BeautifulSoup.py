import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') #Enter the URl
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
y = []
z = []
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    y.append(tag.get('href', None))

print(y[17])

for i in range(6):   
    html = urllib.request.urlopen(y[17], context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        z.append(tag.get('href', None))

    print(z[17])
    y[17] = z[17]
    z = []
