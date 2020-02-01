import requests  
from bs4 import BeautifulSoup

url='https://www.flipkart.com/realme-5s-crystal-purple-128-gb/p/itm592977b0ba210?pid=MOBFM2WZG7AGFGJE&lid=LSTMOBFM2WZG7AGFGJEXD8LE2&marketplace=FLIPKART&srno=b_1_1&otracker=clp_banner_2_3.bannerX3.BANNER_mobiles-republic-day-sale-72d6-29s1-store_CBGA7MUN65WY&fm=neo%2Fmerchandising&iid=45fe1f81-18f3-4367-9ca7-cba5ea2ac76e.MOBFM2WZG7AGFGJE.SEARCH&ppt=browse&ppn=browse&ssid=nzyvpd5fm80000001579588870069'
page=requests.get(url)
bs=BeautifulSoup(page.content,'html.parser')
p=bs.find(class_="_1vC4OE _3qQ9m1").get_text()[1:]
#price=float(p)
print(p)