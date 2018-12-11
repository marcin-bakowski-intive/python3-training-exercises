"""
Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
on the New York Times homepage.
"""

import requests
from bs4 import BeautifulSoup


def get_nytimes_home_page_headings():
    r = requests.get("http://www.nytimes.com")
    soup = BeautifulSoup(r.text, "html5lib")
    return [h2.text for h2 in soup.find_all("h2")]


print("\n".join(get_nytimes_home_page_headings()))
