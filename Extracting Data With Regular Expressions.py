# goal is to scrape/extract all numbers from the file name mbox-short.txt holding unstructured data


import os
# Set the working directory if needed by removing#
#directory= input("working directory path for file:")
#os.chdir(directory)
print("Current Working Directory:", os.getcwd())  # Check if the working directory is correct



name = input("Enter file:")
if len(name) < 1:
    name = "regex_sum_2100259.txt"
fh = open(name)

import re

numbers=[]
numlist=[]


for line in fh:
    line=line.rstrip()
    match= re.findall('[0-9]+',line)
    numlist.extend(match)

for num in numlist:
    number= int(num)
    numbers.append(number)
    
print(sum(numbers))