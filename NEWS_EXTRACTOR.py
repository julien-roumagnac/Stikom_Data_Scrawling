# coding: utf-8

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas
import numpy as np
import requests
import hashlib
import time
from _datetime import datetime

def extract_news(startdate,enddate):
    #connnexion to the DB

    newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')

    #newsletter_db = create_engine('postgres://admin:admin@localhost:5432/newsletter')



    #          <========= TREATMENT FOR NEWS SECTION =========>

    page_link = 'https://gianyarkab.bps.go.id/news.html'
    site_link = 'https://gianyarkab.bps.go.id/'

    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # catching CATEGORY , DATE , DESC from article description
    mydivs = page_content.findAll("div", {"style": "width:96%;padding:10px 2%;"})
    div = mydivs[0]
    description = div.text
    print(div.text)
    children = div.findChildren("img", recursive=False)
    if len(children) > 0 :
        description = children[0].text
    category = None
    desc = None
    date = None
    for i in range(0,len(description)):
        if description[i] == "[" and description[i+ 13] =="]" :
            category = description[i+1:i+4]
            date = description[i+5:i+9] + '-' + description[i+9:i+11] +'-' +description[i+11:i+13]
            desc = description[0:i]

    # catching link to the full article
    fullArticleLink = page_content.findAll("a", {"class": "none"})
    fullArticle = None
    if len(fullArticleLink) > 0:
        fullArticle = site_link + fullArticleLink[0]['href']

    # catching the image of the article
    imageLink = page_content.findAll("img", {"style": "float:left;max-width:50%;padding:0px 10px 10px 0px;"})
    img = None
    if len(imageLink) > 0:
            img = site_link + imageLink[0]['src']

    # catching the title of the article
    titleTags = page_content.findAll("h5", {"class": "judulberita"})
    title = None
    if len(titleTags) > 0 :
        title = titleTags[0].text
    download_link = None

    # printing all catched informations
    if not(title is None):
        print("TITLE : "+ title)
    if not(category is None):
        print("CATEGORY : " + category)
    if not(date is None):
        print("DATE : " + date)
    if not(desc is None):
        print("ARTICLE : " + desc)
    if not(img is None):
        print("IMAGE : " + img)
    if not(fullArticle is None):
        print("FULL ARTICLE LINK : " +  fullArticle)

    if(startdate<datetime.strptime(date, '%Y-%m-%d') and enddate>datetime.strptime(date, '%Y-%m-%d')):
        # Insertion of the news in the DB
        hash_object = hashlib.md5((title+desc).encode())
        id = hash_object.hexdigest()

        publicationDf = pandas.read_sql(("SELECT * FROM publication WHERE id LIKE %s"),newsletter_db,params=[id])
        if(publicationDf.empty):

            newsArray=np.array([[id,desc, time.strftime(date) ,img,category,title[:250],fullArticle,download_link]])
            newsDf=pandas.DataFrame(newsArray, columns = ['id','publication_text','creation_date','imgelink','category','title','full_link','download_link'])
            newsDf.to_sql('publication',newsletter_db,if_exists='append', index=False)
            print('News Inserted !')
    print('END OF NEWS SECTION')

    #           <========= END OF NEWS SECTION =========>




