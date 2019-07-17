# coding: utf-8

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas
import numpy as np
import requests
import hashlib
import time
from datetime import datetime

def publication_extract():
    #connnexion to the DB
    #newsletter_db = create_engine('postgres://admin:admin@localhost:5432/newsletter')
    newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')



    #          <========= TREATMENT FOR PUBLICATION SECTION =========>

    page_link = 'https://gianyarkab.bps.go.id/publication.html'
    # page_link = 'https://gianyarkab.bps.go.id/publication.html?page=3&amp;ajax=yw1'

    site_link = 'https://gianyarkab.bps.go.id/'

    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # catching CATEGORY , DATE , DESC from article description
    mydivs = page_content.findAll("div", {"class": "pub odd col-md-12 col-xs-12 col-sm-12"})
    mydivs += page_content.findAll("div", {"class": "pub even col-md-12 col-xs-12 col-sm-12"})



    for div in mydivs :
        print(div)


        # IMG
        img = div.findAll("img", {"style": "margin-top: 5px;vertical-align: middle;margin-bottom: 10px;width:100%;height:auto;"})
        img = site_link + img[0]['src']
        print("IMG : " + img)

        #TITLE
        title = div.findAll("div", {"class": "thumbnail-judul-publikasi"})
        print("TITLE : " + title[0].text)

        #FULL ARTCILE LINK
        fullArticleLink = title[0].findChildren("a", recursive=False)
        fullArticleLink = fullArticleLink[0]['href']
        print("FULL ARTICLE : " + fullArticleLink)

        # DOWNLOAD LINK
        downloadLink =  div.findAll("a", {"id": "download-publication"})[0]
        downloadLink = site_link + downloadLink['href']
        print("DOWNLOAD LINK : " + downloadLink)

        # ARTICLE TEXT
        articleText = div.findAll("span", {"style": "font-family: Arial, Verdana;"})[0].text
        #articleText = articleText[5:]

        #print('ARTICLE TEXT : ' + articleText)

        while articleText[1] not in 'azertyuiopmlkjhgfdsqwxvbnNBVCXWQSDFGHJKLMPOIUYTREZA' :

            articleText = articleText[1:]

        i=0
        find = False
        while i < len(articleText) and not(find) :

            if articleText[i] == "-" and articleText[i+1] == "-" and articleText[i + 5] == "-"and articleText[i + 14] == "-" and articleText[i + 15] == "-" :
                category = articleText[i + 2:i + 5]
                date = articleText[i + 6:i + 10] + '-' + articleText[i + 10:i + 12] + '-' + articleText[i + 12:i + 14]
                desc = articleText[0:i]
                find = True
            i = i+1
        if(not(find)):
            desc = articleText
            date = datetime.today().strftime('%Y-%m-%d')
            category = '111'

        print("TEXT : " + desc)
        print("DATE : "+ date)
        print("CATEGORY : " + category)








        print("______________________________________________________")



        # Insertion of the publication in the DB
        hash_object = hashlib.md5((title[0].text+desc).encode())
        id = hash_object.hexdigest()

        publicationDf = pandas.read_sql(("SELECT * FROM publication WHERE id LIKE %s"),newsletter_db,params=[id])
        if(publicationDf.empty):

            newsArray=np.array([[id,desc, time.strftime(date) ,img,category,title[0].text[:250],fullArticleLink,downloadLink]])
            newsDf=pandas.DataFrame(newsArray, columns = ['id','publication_text','creation_date','imgelink','category','title','full_link','download_link'])
            newsDf.to_sql('publication',newsletter_db,if_exists='append', index=False)
            print('PUBLICATION Inserted !')
    print('END OF PUBLICATION SECTION')

    #           <========= END OF PUBLICATION SECTION =========>
