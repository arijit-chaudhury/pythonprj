import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
lst = list()

position = input('Enter position:')
count = input('Enter count:')
new_location = int(position) - 1
result = list()

i = 0
while i <= int(count):
    if lst != []:
        url = lst[int(new_location)]
    result.append(url)
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href',None))
    i = i + 1
print(result)