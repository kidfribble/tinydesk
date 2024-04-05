#!/usr/bin/env python3 
#-*- coding: utf-8 -*- 

import sys
import requests
from bs4 import BeautifulSoup

file_name = 'dsnews.txt'

page = requests.get('https://medium.com/@DesignerNews')

soup = BeautifulSoup(page.text, 'html.parser')

domain_index = soup.find("main")

# Get Urls
domain_links = domain_index.find_all('a')

# Create file and save relevant information to it
file = open(file_name, 'wb')

for child in domain_links:
   child.title = child.find('h2')
   if child.title:
     child.link = child.get('href')
     print(' 🟢: ', child.title,
           '\n',
           '🔗: ', child.link)
     child_link = child.link.encode()
     child_title = child.title.encode()
     file.write(child_link + b'\n' + child_title + b'\n')

file.close()