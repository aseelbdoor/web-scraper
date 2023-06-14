import requests
from bs4 import BeautifulSoup


def req(URL):
    pass

def get_citations_needed_count(URL):
    pass


def  get_citations_needed_report(URL):
    pass


URL="https://en.wikipedia.org/wiki/History_of_Mexico"
results=requests.get(URL)
page=BeautifulSoup(results.content,"html.parser")
allPosts=page.find_all("div",class_="hatnote navigation-not-searchable")
header="https://en.wikipedia.org/"
for i in allPosts:
    link=i.find("a").get("href")
    print(header+link)
