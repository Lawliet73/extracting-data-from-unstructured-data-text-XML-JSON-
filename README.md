# Data Parsing, Cleaning, and Analysis Repository

## Overview
This repository contains a series of Python scripts that showcase various techniques for parsing, cleaning, and analyzing different types of data. These scripts demonstrate skills in handling structured and unstructured data in formats like **XML**, **JSON**, **HTML**, and **plain text**, using Python libraries and methods such as **regular expressions**, **BeautifulSoup**, and **urllib**.

Each script retrieves data from a URL or a file, processes and extracts relevant information, and performs specific calculations, like summing numbers from the data. This demonstrates the ability to handle diverse data types, making this repository a valuable showcase of my data parsing and analysis skills for potential employers.

---
## Table of Contents
- [Scripts](#scripts)
  - [Extracting Data from XML](#1-extracting-data-from-xml)
  - [Extracting Data with Regular Expressions](#2-extracting-data-with-regular-expressions)
  - [Scraping Numbers from HTML](#3-scraping-numbers-from-html)
  - [Extracting and Following Links from HTML](#4-extracting-and-following-links-from-html)
  - [Extracting Data from JSON](#5-extracting-data-from-json)
- [How to Run the Scripts](#how-to-run-the-scripts)
- [Author](#author)

---

## Scripts

### 1. **Extracting Data from XML**
- **Goal**: Retrieve XML data from a URL, parse it, and extract numerical values from specific XML tags.
- **Libraries Used**: `urllib`, `xml.etree.ElementTree`
- **Approach**: 
  - Prompts for a URL and retrieves the XML data.
  - Parses the XML to find specific elements containing numbers.
  - Computes the sum of the extracted values.
  
  **Script**: [Extracting Data from XML](Extracting%20Data%20from%20XML.py)
  
  **Sample Code**:
  ``python
  url = "http://py4e-data.dr-chuck.net/comments_2100263.xml"
  tree = ET.fromstring(xmldata)  
  numbers = tree.findall(".//count")  
  summe = sum([int(num.text) for num in numbers]) ``


### 2. Extracting Data with Regular Expressions

- **Goal**: Extract numbers from unstructured plain text files using regular expressions and compute their sum.

- **Libraries Used**: re

- **Approach**:

- Opens and reads a file.
- Uses regular expressions to find all numerical patterns.
- Converts the extracted strings into integers and calculates their sum.
- Script: Extracting Data With Regular Expressions

**Sample Code**:
``python match = re.findall('[0-9]+', line)
numbers = [int(num) for num in match]
print(sum(numbers)) ``


### 3. Scraping Numbers from HTML
- **Goal**: Extract numbers from HTML files and compute their sum.

- **Libraries Used**: BeautifulSoup, urllib, re

- **Approach**:

- Retrieves an HTML page using urllib.
- Uses BeautifulSoup to parse the HTML and extract relevant data enclosed in specific HTML tags (e.g., <span>).
- Uses regular expressions to find numerical values and calculates their sum.
- Script: Scraping Numbers from HTML

Sample Code:
``python match = re.findall(r'<span[^>]*>([0-9]+)</span>', html_str)
numlist = [int(num) for num in match]
print(sum(numlist))``


### 4. Extracting and Following Links from HTML
- **Goal**: Follow a series of links from an HTML page, retrieve specific link data, and extract a final result.

- **Libraries Used**: BeautifulSoup, urllib, re

- **Approach**:

- Retrieves an HTML page and uses BeautifulSoup to extract all links (<a> tags).
- Follows the links a specific number of times to find the final target page.
- Extracts a name from the final page using regular expressions.
- Script: Extracting and Following Links from HTML

Sample Code:
``
python
soup = BeautifulSoup(html, "html.parser")
tags = soup.find_all("a")
correctlink = tags[finalposition - 1].get("href") ``


### 5. Extracting Data from JSON
- **Goal**: Retrieve JSON data from a URL, parse it, extract numerical values from the JSON structure, and compute their sum.

- **Libraries Used**: json, urllib

- **Approach**:

- Prompts for a URL and retrieves the JSON data.
- Parses the JSON to extract numerical values from a specific key.
- Computes the sum of the extracted values.
- Script: Extracting Data from JSON

Sample Code:
``
python
data = json.loads(jasondata)
numbers = [comment["count"] for comment in data["comments"]]
print(sum(numbers)) ``


### How to Run the Scripts
1.Install Required Libraries:
   Make sure you have the required Python libraries installed: for example
``pip install beautifulsoup4``

2.Run the Scripts:
Each script can be run from the command line. For example:
``
python Extracting\ Data\ from\ XML.py``

3.Modify the URL or File Input:
Each script prompts for a URL or file path. You can modify the default input values to test different datasets or web pages.


### Author
Kalab Alemayehu



