import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/index.html"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")

book_container = []
price_container = []
for page in range(1,51):
    link_url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    sub_response = requests.get(link_url)
    sub_soup = BeautifulSoup(sub_response.text,"html.parser")
    box = sub_soup.find("ol",class_="row")
    article = box.find_all("article",class_="product_pod")
    for book in article:
        title = book.select_one("h3 a").text.strip()
        price = book.find("p",class_="price_color").text.strip()
        book_container.append(title)
        price_container.append(price)
df = pd.DataFrame({
    "Books":book_container,
    "Price":price_container})
df.to_csv("books_to_scrape.csv",index=False)
print (len(book_container))
print (len(price_container))
print ("Books Data Saved Sucessfully!!!")
