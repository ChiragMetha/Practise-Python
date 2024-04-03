# Decode A Web Page Solutions
# Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.
import requests
from bs4 import BeautifulSoup
baseurl = 'http://www.nytimes.com'
r = requests.get(baseurl)
soup = BeautifulSoup(r.text, 'html.parser')

for story_heading in soup.find_all(class_="indicate-hover"):
    if story_heading.p:
        print(story_heading.p.text.replace("\n", "").strip())
    else:
        print(story_heading.contents[0].strip())