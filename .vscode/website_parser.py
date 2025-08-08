"""
Task:
1. Crawl the website and get the list of all the issues.
https://www.google.com 
Date - 2023-08-29
Created by - @anna
""" 
import requests  # for making HTTP requests
from bs4 import BeautifulSoup  # for parsing HTML
from urllib.parse import urljoin    # for joining URLs

url = "https://www.google.com" # website for parsing
getrequest = requests.get(url) 
soup = BeautifulSoup(getrequest.text, 'html.parser') 

if getrequest.status_code == 200:  # checking response status
  for link in soup.find_all('a', href=True):  # finding all links
    full_url = urljoin(url, link['href'])  # getting URL
    print("Done ✅ HTTP 200 -  link is working",  full_url)
else:
  print("Error ❌ HTTP 404 - link is not working", url)
  