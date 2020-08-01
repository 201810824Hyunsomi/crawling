from bs4 import BeautifulSoup
import urllib.request
import requests
soup = BeautifulSoup(urllib.request.urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EC%A2%85%EB%A1%9C%EA%B5%AC+%ED%99%8D%EC%A7%80%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EC%A4%91%EB%9E%91%EA%B5%AC+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80").read(), 'html.parser')

if __name__  == "__main__":
    soup=BeautifulSoup(urllib.request.urlopen("https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EC%A2%85%EB%A1%9C%EA%B5%AC+%ED%99%8D%EC%A7%80%EB%8F%99+%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8+%EC%A4%91%EB%9E%91%EA%B5%AC+%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80").read(), 'html.parser')
    res=soup.find_all("u1","list_area")   
    for n in res:
        print(n.get_text())
