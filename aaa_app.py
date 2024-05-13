import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import logging
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

options=webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

product="iphone 13"
search_str=f"/search?q={'+'.join(product.split(' '))}"
baseurl="https://www.flipkart.com"

driver.get(baseurl+search_str)

search_html=bs(driver.page_source,'html.parser')

products=search_html.find_all('div',{'class':'cPHDOP col-12-12'})[2:-4]

productsUrl_list=[]
for  product in products:
    productsUrl_list.append(baseurl+str(product.div.div.div.a['href']))

driver.get(productsUrl_list[0])
productDetail_html=bs(driver.page_source,'html.parser')
print(productDetail_html.find("span",{"class":"VU-ZEz"}).text)
commentBoxes=productDetail_html.find_all("div",{"class":"col EPCmJX"})

for commentBox in commentBoxes:
    name=commentBox.find_next("div",{"class":"row gHqwa8"})
    ratingComment=name.parent.find_all("div",{"class":"row"})
    rating,comment=ratingComment[0],ratingComment[1]
    print(name.div.p.text)
    print(rating.div.text)
    print(rating.p.text)
    print(comment.div.div.div.text)




"""names_list=productDetail_html.find_all("p",{"class":"_2NsDsF AwS1CA"})
ratings_list=productDetail_html.find_all("div",{"class":"XQDdHH Ga3i8K"})
comments_list=productDetail_html.find_all("div",{"class":"ZmyHeo"})
commentsHead_list=productDetail_html.find_all("p",{"class":"z9E0IG"})

print(names_list[0].text)
print(ratings_list[0].text)
comment_withBR=comments_list[0].div.div
comments_list
c=comment_withBR.findAll("br")
fcomment=comment_withBR.text
for comment in c:
    fcommment=fcomment+comment.text+"\n"
print(commentsHead_list[0].text)
print(fcomment)
filename=search_str+".csv"
fw=open
"""









