from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'price': [], 'link':  []}

# Convert data into csv file
for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        h = soup.find("h2")   # Gives title of product
        title =h.get_text()
        
        l = h.find("a")
        link = "https://amazon.in/" + l['href'] # Gives link of product

        p = soup.find("span", attrs={'class': 'a-price-whole'}) # Gives price of product
        price = p.get_text()

        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)
    except Exception as e:
        print(e)
# make csv file.
df = pd.DataFrame(data=d)
df.to_csv("data.csv")