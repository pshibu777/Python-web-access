import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
counts=input('Enter counts:')
counts=int(counts)
counts=counts+5
position=input('Enter position:')
position=int(position)
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(counts):
    link = tags[position].get('href', None)
    position = position+1
    print("Retrieving:",link)
