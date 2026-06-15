import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"}
url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav"

response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,"html.parser")
# print (soup.prettify)
titles = []
ratings = []
descriptions = []
values = []
company_list = soup.find("div",class_="col-left")
companies = company_list.find_all("div",class_="companyCardWrapper")
total = 0
for company in companies:
    name = company.find("h2").text.strip()
    rating = company.find("div",class_="rating_text").text.strip()
    about = company.find("span",class_="companyCardWrapper__interLinking").text.strip()
    value = company.find_all("span",class_="companyCardWrapper__ratingValues")
    try:
        highly_rated = values[0].text.strip()
        if highly_rated:
            print (f"Highly Rated For : {highly_rated}")
        negatively_rated = values[1].text.strip()
        if negatively_rated:
            print (f"Critically Rated For : {negatively_rated}")
    except:
        pass
    titles.append(name)
    ratings.append(rating)
    descriptions.append(about)

df = pd.DataFrame({
        "Company":titles,
        "Description":descriptions,
        "Rating":ratings, })
df.to_csv("Company_list.csv",index=False)
print (""Saved Sucessfully !!!)
