



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
    url = "http://py4e-data.dr-chuck.net/known_by_Nathan.html"



finalcount= 8
finalposition= 18
currentcount= 0
correctlink=()



while currentcount < finalcount:
    
    html= urllib.request.urlopen(url).read()
    soup= BeautifulSoup(html,"html.parser")
    tags=soup.find_all("a")
    print(f"Retrieving:{url}")
    
    currentposition = 0
    
    for tag in tags:
        currentposition+=1
    
        
        if currentposition == finalposition:
            correctlink= tag.get("href")
            url=correctlink
            break
        
    currentcount += 1
        
namein= str(correctlink)
name=re.findall(r"^by_([A-Za-z]+)\.html",namein)
print(f"Last name: {name[0]}")

        
        
    
    