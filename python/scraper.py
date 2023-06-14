import requests
from bs4 import BeautifulSoup


def req(URL):
    results=requests.get(URL)
    page=BeautifulSoup(results.content,"html.parser")
    allParagraph=BeautifulSoup(str(page.find_all("div",class_="mw-parser-output")),"html.parser")
    test=allParagraph.find_all("p")
    li=[]
    for i in test:
        link=i.find("span")
        if link is not None:
            li.append(i)
    return li
    

def get_citations_needed_count(URL):
    allP=req(URL)
    return len(allP)


def  get_citations_needed_report(URL):
    allP=req(URL)
    st=""
    for i in allP:
        txt=i.text
        st+=(str(txt).strip()+"\n\n")
    return st.strip()


if __name__=="__main__":
    URL="https://en.wikipedia.org/wiki/History_of_Mexico"
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
