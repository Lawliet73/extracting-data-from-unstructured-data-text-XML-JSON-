# goal of this python program is to prompt for a URL,read the retrieved JSON data from that URL using urllib
# and then parse and extract the comment counts from the JSON data and compute the sum of the 
#numbers in the file

import os
# Set the working directory if needed by removing#
#directory= input("working directory path:")
#os.chdir(directory)
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct



import urllib.request, urllib.parse, urllib.error
import json, ssl

url= input("Enter  URL")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_2100264.json"
    
    

html= urllib.request.urlopen(url)
jasondata=html.read().decode()
print('Retrieved',len(jasondata),'characters')
data = json.loads(jasondata)
list= data["comments"]




numbers=[]
summe=int()
x=0

#print(json.dumps(data,indent=4))

for comment in list:
    
    name=comment["name"]
    number= comment["count"]
    numbers.append(number)
    
    
    
print("found",len(numbers),"counts")

summe=sum(numbers)
    
print("sum is:",summe)

    