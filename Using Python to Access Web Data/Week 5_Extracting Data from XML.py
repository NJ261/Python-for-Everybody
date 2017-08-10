import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

m = 0
address = input('Enter location: ')

print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
print('Retrieved', len(data), 'characters')

y = BeautifulSoup(data, "xml")
tags = y('count')

y = (re.findall('[0-9]+',str(tags)))
y = list(map(int, y))   
print ("Count: ", len(y))

for i in y:
    m = i + m
print("Sum: ", m)