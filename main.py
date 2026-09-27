import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/page/"

with open("quotes.txt", "w") as file:
    for i in range(1, 11):
        soup = BeautifulSoup(requests.get(url + str(i)).text, "html.parser")
        for quote in soup.select("div.quote"):
            text = quote.select_one(".text").get_text()
            author = quote.select_one(".author").get_text()
            file.write(f"{text} — {author}\n")
