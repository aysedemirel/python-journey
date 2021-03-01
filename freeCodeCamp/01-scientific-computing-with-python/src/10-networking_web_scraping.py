# What is Web Scraping ?
# When a program or script pretends to be a browser and retrieves web pages, 
# looks at those web pages, extracts information,
# and then looks at more web pages

# Search engines scrape web pages 
# we call this "spidering the web" or "web crawling"

# Web Scraping -> The easy way - Beautiful Soap 

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter - ') # http://www.dr-chuck.com/page1.htm
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))