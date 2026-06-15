import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}
url = "https://www.accuweather.com/en/in/mumbai/204842/weather-forecast/204842"
response = requests.get(url,headers = headers)
soup = BeautifulSoup(response.text,"html.parser")
# print (soup)
container = soup.find("div",class_="cur-con-weather-card__body")
# print (container)
contains = container.find_all("div",class_="spaced-content detail")

lhs_side = []
rhs_side = []

for contain in contains:
    rhs = contain.find("span",class_="label")
    lhs = contain.find("span",class_="value")
    rhs_side.append(rhs)
    lhs_side.append(lhs)
    
df = pd.DataFrame({"rhs_side" : rhs_side,
                   "lhs_side" : lhs_side})
df.to_csv("weather.csv",index=False)

# py weather_scraper.py
