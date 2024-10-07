# goal is to scrape/extract all the numbers in the file name mbox-short.txt holding HTML response
#and print their sum

import os
# Set the working directory if needed by removing#
#directory= input("working directory path:")
#os.chdir(directory)
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct



import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re

url= input("Enter  URL")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.html"

html= urllib.request.urlopen(url).read()
soup= BeautifulSoup(html,"html.parser")

numlist=[]
html_str= str(soup)

match= re.findall(r'<span[^>]*>([0-9]+)</span>',html_str)

for num in match:
    numlist.append(int(num))
    
print(sum(numlist))





