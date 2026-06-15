import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://timesofindia.indiatimes.com/home/headlines"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
news_page = soup.find("div",id="c_headlines_wdt_1")
header = news_page.select_one("h1 span").text
headlines = news_page.find_all("li")
highlight = []
for headline in headlines:
    heading = headline.select_one("span a").text.strip()
    highlight.append(heading)
print (len(headlines))

df = pd.DataFrame({"headings":heading})
# py news_scraper.py
