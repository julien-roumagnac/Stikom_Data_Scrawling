# coding: utf-8

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas
import numpy as np
import requests
import hashlib
import time
from datetime import datetime

def pressrelease_extract(startdate,enddate):
    #connnexion to the DB
    #newsletter_db = create_engine('postgres://admin:admin@localhost:5432/newsletter')
    newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')



    #          <========= TREATMENT FOR PRESSRELEASE SECTION =========>


    page_link = 'https://gianyarkab.bps.go.id/pressrelease.html'

    site_link = 'https://gianyarkab.bps.go.id/'

    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")

    # Catching all the articles from the page

    mydivs = page_content.findAll("td", {"style": "display: list-item;margin-left:25px;width:auto;text-align:justify;"})



    for div in mydivs :
        # catching link to full article to take the data on this link
        children = div.findChildren("a", recursive=False)
        articlelink = children[0]['href']
        print('FULL LINK : ' + articlelink)

        # taking the html content of the full article page
        article_response = requests.get(articlelink, timeout=5)
        article_content = BeautifulSoup(article_response.content, "html.parser")

        # catching the title
        titleTags = article_content.findAll("h4", {"class": "judulberita"})
        title = None
        if len(titleTags) > 0:
            title = titleTags[0].text
        print('TITLE : ' + title)
        # imagelink
        img = None

        category = None
        desc = None
        date = None
        description = article_content.findAll("span", {"style": "font-size: 13.3333px;"})[0].text
        for i in range(0, len(description)):
            if description[i] == "[" and description[i + 13] == "]":
                category = description[i + 1:i + 4]
                date = description[i + 5:i + 9] + '-' + description[i + 9:i + 11] + '-' + description[i + 11:i + 13]
                desc = description[0:i]

        if category is None:
            category = '111'
        print("CATEGORY : " + category)
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')
        print("DATE : " + date)
        if desc is None:
            desc= description
        print("ARTICLE : " + desc)
        # DOWNLOAD LINK
        downloadLink = article_content.findAll("a", {"id": "download-brs"})[0]
        downloadLink = site_link + downloadLink['href']
        print("DOWNLOAD LINK : " + downloadLink)

        print('_____________')

        if (startdate < datetime.strptime(date, '%Y-%m-%d') and enddate > datetime.strptime(date, '%Y-%m-%d')):
            # Insertion of the news in the DB
            hash_object = hashlib.md5((title + desc).encode())
            id = hash_object.hexdigest()

            publicationDf = pandas.read_sql(("SELECT * FROM publication WHERE id LIKE %s"), newsletter_db, params=[id])
            if (publicationDf.empty):
                newsArray = np.array([[id, desc, time.strftime(date), img, category, title[:250], articlelink, downloadLink]])
                newsDf = pandas.DataFrame(newsArray,
                                          columns=['id', 'publication_text', 'creation_date', 'imgelink', 'category', 'title',
                                                   'full_link', 'download_link'])
                newsDf.to_sql('publication', newsletter_db, if_exists='append', index=False)
                print('PRESS RELEASE Inserted !')

    print('END OF PRESS RELEASE SECTION')
