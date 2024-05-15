import time
import logging
from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import  webdriver

app=Flask(__name__)


@app.route("/",methods=['GET'])
def homepage():
    return render_template("index.html")

@app.route("/review",methods=['POST','GET'])
def index():
    if request.method=='POST':
        searchString="+".join(request.form['content'].split())
        flipkartUrl="https://www.flipkart.com/search?q=" + searchString
        driver.get(flipkartUrl)
        time.sleep(3)
        search_html=bs(driver.page_source,'html.parser')
        products = search_html.find_all('div', {'class': 'cPHDOP col-12-12'})[2:-4]
        productsUrl_list = []
        for product in products:
            productsUrl_list.append("https://www.flipkart.com" + str(product.div.div.div.a['href']))

        filename = searchString + ".csv"
        fw = open(filename, "w")
        headers = "ProductName, CustomerName, Rating , CommentHeader,Comment \n"
        fw.write(headers)
        reviews = []
        for link in productsUrl_list:
            try:
                driver.get(link)
                time.sleep(3)
                product_html=bs(driver.page_source,"html.parser")
                productname=product_html.find("span",{"class":"VU-ZEz"}).text
                commentBoxes=product_html.find_all("div",{"class":"col EPCmJX"})
                for commentBox in commentBoxes:
                    try:
                        nameBox = commentBox.find_next("div", {"class": "row gHqwa8"})
                        ratingComment = nameBox.parent.find_all("div", {"class": "row"})
                        ratingDiv, commentdiv = ratingComment[0], ratingComment[1]
                        name=nameBox.div.p.text
                        rating=ratingDiv.div.text
                        ratingHead=ratingDiv.p.text
                        comment=commentdiv.div.div.div.text
                    except Exception as e:
                        logging.info(e)
                    mydict={"ProductName":productname,"CustomerName":name,"Rating":rating,"CommentHeader":ratingHead,"Comment":comment}
                    reviews.append(mydict)
                logging.info(f"logging my final dict result as {reviews}")
                uri="mongodb+srv://admin:admin@cluster0.qm6mxz1.mongodb.net/?retryWrites=true&w=majority&appName = Cluster0"
                # Create a new client and connect to the server
                client = MongoClient(uri, server_api=ServerApi('1'))
                # Send a ping to confirm a successful connection
                try:
                    client.admin.command('ping')
                    logging.info("Pinged your deployment. You successfully connected to MongoDB!")
                    database=client['flipkart_reviews']
                    dbclient=database["scrapper_flipkart_reviews"]
                    dbclient.insert_many(reviews)
                except Exception as e:
                    logging.info(e)
                return render_template('result.html',reviews=reviews[0:(len(reviews)-1)])
            except Exception as e:
                logging.info(e)
                return "something went wrong!!!!"
        else:
            return render_template("index.html")


if __name__=="__main__":
    logging.basicConfig(filename="scrapper.log", level=logging.INFO)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    app.run(host="0.0.0.0")




