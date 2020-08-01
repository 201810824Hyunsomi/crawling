from bs4 import BeautifulSoup as bs
import requests

url ='https://www.siksinhot.com/P/254092'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
plain_text = response.text
soup = bs(plain_text, 'lxml')
name=soup.find('h3',{'data-reactid':'59'})
print(name.text)
reviews=soup.find_all('div',{'class':'score_story'})
for i in range(0,len(reviews),1):
  print(i+1,end=" ")
  print( "번째 리뷰 평점과 평가: " + reviews[i].text)
file=open('food_review.txt','w',encoding='utf-8')
file.write(name.text+"맛 평가"+"\n")
for i in range(0,len(reviews),1):
    file.write(str(i+1)+"번째 리뷰:   ")
    file.write(reviews[i].text)
    file.write("\n")
file.close()
