# goal of this python program is to prompt for a URL,read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data and compute the sum of the 
#numbers in the file


import os
# Set the working directory if needed by removing#
#directory= input("working directory path:")
#os.chdir(directory)
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct



import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import re

url= input("Enter  URL")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2100263.xml"
    

html= urllib.request.urlopen(url)
xmldata=html.read()
print('Retrieved',len(xmldata),'characters')
tree = ET.fromstring(xmldata)


numbers=tree.findall(".//count")
print("found",len(numbers),"counts")
summe=int()

for num in numbers:
    count=num.text  
    number=int(count)
    summe+=number

    
print("summe=",summe)
    
    
    
    