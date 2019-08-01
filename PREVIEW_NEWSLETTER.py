from sqlalchemy import create_engine
import pandas
import NEWSLETTER_SENDER as NS
import numpy as np
import hashlib
import time

newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')

categories = ['001','010','100','111','110','101','011']

for userCategory in categories :
    print("CATEGORY : "+ userCategory)
    usersSameCategoryDf = pandas.read_sql(("SELECT * FROM user_newsletter as u where prefbroadcast = '"+userCategory+"'"), newsletter_db)
    print()

    if (usersSameCategoryDf.shape[0]>0):
        print("USERS OF THIS CATEGORY")
        print(usersSameCategoryDf)

        userId = usersSameCategoryDf.values[0][0]
        userName = usersSameCategoryDf.values[0][1]
        userPhone = usersSameCategoryDf.values[0][2]
        userEmail = 'gianyarkab.newsletter@gmail.com' # addres to receive the preview of the newsletter for all categories
        userCategory = usersSameCategoryDf.values[0][4]
        userDate = usersSameCategoryDf.values[0][11]
        print()
        # detecting what are the categories that interest him
        userCategories = ''
        if userCategory == '000':
            userCategories = "p.category = '000'"
        if userCategory == '001':
            userCategories = " p.category ='001' or p.category = '111' "
        if userCategory == '010':
            userCategories = " p.category ='010' or p.category = '111' "
        if userCategory == '100':
            userCategories = " p.category ='100' or p.category = '111' "
        if userCategory == '011':
            userCategories = " p.category ='001' or p.category ='010' or p.category = '111' "
        if userCategory == '101':
            userCategories = " p.category ='001' or p.category ='100' or p.category = '111' "
        if userCategory == '110':
            userCategories = " p.category ='100' or p.category ='010' or p.category = '111' "
        if userCategory == '111':
            userCategories = " p.category ='001' or p.category ='010'or p.category ='100' or p.category = '111' "

        # we load all the publications that interest him and he never receive from the newsletter
        userPublicationsDf = pandas.read_sql(
            ("SELECT * FROM publication as p WHERE (" + userCategories + ") and creation_date > '" + userDate.strftime(
                '%Y-%m-%d') + "' and p.id not in ( SELECT news_id from flags where user_id = '" + userId + "') ORDER BY creation_date "),
            newsletter_db)
        print("PUBLICATIONS FOR THIS CATEGORY : ")
        for userpubs in userPublicationsDf.values:
            print(userpubs[2].strftime('%Y-%m-%d') + " : " + userpubs[4] + " , " + userpubs[5])

        if (userPublicationsDf.shape[0] > 2):

            print("At least 3 publications so we send an email to : " + userCategory)
            publications = []
            # we collect the 3 oldest publications
            for i in range(0, 3):
                publications.append(userPublicationsDf.values[i])

            # sending of the 3 publication to the user
            NS.send_newsletter(userCategory, userEmail, publications)