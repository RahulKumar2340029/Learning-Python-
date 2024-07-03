import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# for url in url_lists:
#     webbrowser.open_new_tab(url)

import requests

# url = 'https://github.com/RahulKumar2340029/30-Days-Of-Python/blob/master/20_Day_Python_package_manager/20_python_package_manager.md'
# response = requests.get(url)
# print(response)
# print(response.headers)
# print(response.content)

'''eg.2'''
# url = 'https://restcountries.com/v3.1/all'
# response = requests.get(url)
# print(response)
# print(response.json()[:1])

from collections import Counter
import re
# url = 'https://www.gutenberg.org/cache/epub/1513/pg1513.txt'
# response = requests.get(url)
# txt = response.text
#
# cleaned_text = re.sub(r'[^a-zA-Z\s]', '', txt).lower()
#
# words = cleaned_text.split()
#
# word_count = Counter(words)
# most_common_words = word_count.most_common(10)
# print(most_common_words)


'''problem 2'''
import statistics
# url = 'https://api.thecatapi.com/v1/breeds'
# response = requests.get(url)
# data = response.json()


from bs4 import BeautifulSoup

# Fetch the HTML content of the webpage
url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
html_content = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table element



