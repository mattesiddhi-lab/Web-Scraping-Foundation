import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com/"
response = requests.get(url)
quote_scrapped = []
name_scrapped = []
for i in range(11):
    link = f"{url}/page/{i}/"
    response = requests.get(link)
    soup = BeautifulSoup(response.text,"html.parser")
    container = soup.find("div",class_="container")
    title = soup.find("h1").text.strip()
    # print (f"Title:{title}")
    quotes = container.find_all("div",class_="row")[1]
    quote_lines = quotes.find_all("div",class_="quote")
    for quote in quote_lines:
        slogan = quote.find("span",class_="text").text.strip()
        author = quote.find("small",class_="author").text.strip()
        quote_scrapped.append(slogan)
        name_scrapped.append(author)
df = pd.DataFrame({
    "Author":name_scrapped,
    "Quote":quote_scrapped
})
df.to_csv("quotes.csv")
