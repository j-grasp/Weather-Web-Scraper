import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}

def weather_tampa():
    #components to parse weather.com
    weather_tampa_url="https://weather.com/weather/today/l/3fcb01b2e7fc39868a8e84bc94d22312e20b610e686585b630e1f472171931c4"
    page = requests.get(weather_tampa_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #finding info on page
    current_temp = soup.find(class_='_3KcTQ')
    high_low = soup.find(class_='_23DP5')
    rain_chance = soup.find(class_='RBVJT')

    #print info
    print(current_temp.get_text())
    print(high_low.get_text())
    print(rain_chance.get_text())


def main():
    weather_tampa()


main()