import requests
from bs4 import BeautifulSoup as bs
url1 = """https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EC%84%9C%EC%B4%88%EA%B5%AC+%EB%B0%A9%EB%B0%B0%EB%8F%99+%EB%82%A0%EC%94%A8"""
html = requests.get(url1)
plain_text = html.text
soup = bs(plain_text, 'lxml')
area = soup.find('span', {'class': 'btn_select'}).find('em')
today_temperature=soup.find('p',{'class':'info_temperature'}).find('span',{'class':'todaytemp'})
today_weather=soup.find('p',{'class':'cast_txt'})
min_temp = soup.find('span', {'class': 'min'})
max_temp = soup.find('span', {'class': 'max'})
sensible_temp=soup.find('span',{'class':'sensible'})
weathers=soup.find_all('dd',{'class':'weather_item _dotWrapper'},'span')
weathers_time=soup.find_all('dd',{'class':'item_time'})
tomorrow_temperature=soup.find('div',{'class':'tomorrow_area _mainTabContent'}).find('div',{'class':'main_info morning_box'}).find('p',{'class':'info_temperature'}).find('span',{'class':'todaytemp'})
weather = soup.find('div',{'class':'tomorrow_area _mainTabContent'}).find('div',{'class':'main_info morning_box'}).find('p', {'class': 'cast_txt'})
wind_speed = soup.find("div", {'class': 'info_list wind _tabContent'})
humidity = soup.find("div", {'class': 'info_list humidity _tabContent'})
today_rainforest_possibility=soup.find('li',{'class':'date_info today'}).find('span',{'class':'point_time morning'}).find('span',{'class':'rain_rate'}).find('span',{'class':'num'})
rainforest_possibility=soup.find_all('li',{'class':'date_info today'},'num')
tomorrow_rainforest_possibility=rainforest_possibility[1].find('span',{'class':'num'})
day_after_tomorrow_rainforest_possibility=rainforest_possibility[2].find('span',{'class':'num'})
fine_dust=soup.find('dd',{'class':'lv2'}).find('span',{'class':'num'})
ozon=soup.find('dd',{'class':'lv1'}).find('span',{'class':'num'})
if area is not None:
    print("지역: "+area.text)
else:
    print("Area is none!")
    area = ""
if today_temperature is not None:
    print("현재 온도: "+today_temperature.text)
else:
    print("today_temperature is none!") 
    today_temperature = ""
if sensible_temp is not None:
    print("체감 온도: "+sensible_temp.text)
else:
    print("sensible_temp is none!") 
    sensible_temp = ""
if today_weather is not None:
    print("현재 날씨: "+today_weather.text)
else:
    print("today_weather is none!") 
    today_weather = ""
if min_temp is not None:
    print("최저 온도: "+min_temp.text[:-1])
else:
    print("Min temp is none!")
    min_temp = -1
if max_temp is not None:
    print("최고 온도: "+max_temp.text[:-1])
else:
    print("max temp is none!")
    max_temp = -1
if tomorrow_temperature is not None:
    print("내일 온도: "+tomorrow_temperature.text)
else:
    print("tomorrow_temperature is none!")
    tomorrow_temperature = ""
if weather is not None:
    print("내일 날씨: "+weather.text.split(',')[0])
else:
    print("weather is none!")
    weather = ""
if wind_speed is not None:
    print("풍속: "+wind_speed.text.strip().split()[2][:-3])
else:
    print("wind_speed is none!")
    wind_speed = ""
if humidity is not None:
    print("습도: "+humidity.text.strip().split()[2][:-1])
else:
    print("humidity is none!")
    humidity = ""
if today_rainforest_possibility is not None:
    print("오늘 강수예측량: "+today_rainforest_possibility.text)
else:
    print("today_rainforest_possibility is none!")
    today_rainforest_possibility = ""
if tomorrow_rainforest_possibility is not None:
    print("내일 강수예측량: "+tomorrow_rainforest_possibility.text)
else:
    print("tomorrow_rainforest_possibility is none!")
    tomorrow_rainforest_possibility = ""
if day_after_tomorrow_rainforest_possibility is not None:
    print("모레 강수예측량: "+day_after_tomorrow_rainforest_possibility.text)
else:
    print("day_after_tomorrow_rainforest_possibility is none!")
    day_after_tomorrow_rainforest_possibility = ""
if fine_dust is not None:
    print("미세먼지: "+fine_dust.text)
else:
    print("fine_dust is none!")
    fine_dust = ""
if ozon is not None:
    print("오존: "+ozon.text)
else:
    print("ozon is none!")
    ozon = ""
weather_list=["날씨정보","지역: ",area.text,"현재 온도: ",today_temperature.text,"체감 온도: ",sensible_temp.text,"현재날씨: ",today_weather.text,"최저 온도: ",min_temp.text[:-1],"최고 온도: ",max_temp.text[:-1],"내일 온도: ",tomorrow_temperature.text,"내일 날씨: ",weather.text,"풍속: ",wind_speed.text.strip().split()[2][:-3],"습도: ",humidity.text.strip().split()[2][:-1],"오늘 강수예측량: ",today_rainforest_possibility.text,
              "내일 강수예측량: ",tomorrow_rainforest_possibility.text,"모레 강수예측량: ",day_after_tomorrow_rainforest_possibility.text,"미세먼지: ",fine_dust.text,"오존: ",ozon.text]
file=open('weather.txt','w',encoding='utf-8')
for i in weather_list:
    file.write(i)
    file.write('\n')
file.close()
