import requests
from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

#number of books on page 1
books = soup.find_all("article", class_="product_pod")


#extract title and price of one book
book = books[0]
title = book.find("h3").find("a")["title"]
price = book.find("p", class_="price_color").text


#extract all books
book_data=[]
for book in books:
    title=book.h3.a["title"]
    price=book.find("p", class_="price_color").text
    book_data.append([title, price])


#create a dataframe
import pandas as pd
df= pd.DataFrame(book_data, columns=["Title", "Price"])


df.to_csv("books.csv", index=False)

for page in range(1, 6):
    url=f"https://books.toscrape.com/catalogue/page-{page}.html"