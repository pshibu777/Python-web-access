from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum=0
counts=0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    #print('Contents:', tag.contents[0])
    contents = tag.contents[0]
    contents = int(contents)
    #contents = contents.astype(int)
    #sum = sum+contents
    sum = sum+contents
    counts=counts+1
print(counts)
print(sum)
