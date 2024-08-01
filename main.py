from bs4 import BeautifulSoup
import requests
import pprint

#url = "file:///D:/GitHub/Python/PS01/Index.html"
url = "http://quotes.toscrape.com/"
response =requests.get(url)
print(response.content)
html = response.text

soup = BeautifulSoup(html, "html.parser")

text = soup.find_all("span", class_="text")
print(text)


