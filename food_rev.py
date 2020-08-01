from selenium import webdriver
import time
url1='https://www.diningcode.com/profile.php?rid=9dLu0XN8Lk1g'
url2='https://www.diningcode.com/profile.php?rid=57ZtJeqnveve'
url3='https://www.diningcode.com/profile.php?rid=YiawnMLQS7EP'
url4='https://www.diningcode.com/profile.php?rid=elf007aU0Prf'
url5='https://www.diningcode.com/profile.php?rid=AYQsX9L0k2oA'
url6='https://www.diningcode.com/profile.php?rid=cqWqoaUsDPYH'
url7='https://www.diningcode.com/profile.php?rid=7hqDEV1BnEbk'
url8='https://www.diningcode.com/profile.php?rid=ECucMx3YQmVd'
url9='https://www.diningcode.com/profile.php?rid=7BGMZuWt0dcu'
url10='https://www.diningcode.com/profile.php?rid=EfLhfp7v7wol'
urls=[url1,url2,url3,url4,url5,url6,url7,url8,url9,url10]
for i in range(len(urls)):
    driver=webdriver.Chrome("C:/Users/KDG/Downloads/chromedriver_win32./chromedriver.exe")
    driver.implicitly_wait(3)
    driver.get(urls[i])
    while True:
        try:
            더보기 = driver.find_element_by_css_selector('#div_more_review')
            더보기.click()
            time.sleep(1)
        except:
            break
    name=driver.find_element_by_css_selector('.tit-point')
    body = driver.find_elements_by_css_selector('div >p.review_contents.btxt')
    #print("< 리뷰 개수(개) : "+ str(len(body))+" >")
    grade=driver.find_element_by_css_selector('.grade')
    info=driver.find_elements_by_css_selector('.short')
    for content in body:
        print(content.text)
        print(" ")
    text_review=driver.find_elements_by_css_selector('.review_contents btxt')
    time.sleep(5)
    #print("리뷰 끝")
    driver.quit()