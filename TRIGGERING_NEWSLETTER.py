from sqlalchemy import create_engine
import pandas
import NEWSLETTER_SENDER as NS
import numpy as np
import hashlib
import time

def trigger_and_mail():
    # connnexion to the DB
    #newsletter_db = create_engine('postgres://admin:admin@localhost:5432/newsletter')
    newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')

    # retrieval of publication data from the DB

    publicationsDf = pandas.read_sql(("SELECT * FROM publication order by creation_date "),newsletter_db)
    print('ALL PUBLICATIONS ALLREADY SCRAWLED ORDER BY DATE')
    print()
    for publi in publicationsDf.values :
        print(publi[2].strftime('%Y-%m-%d')+" : "+publi[5]+", "+publi[4]+";")

    print()
    print("OLDEST SCRAWLED PUBLICATION DATE : "+ publicationsDf.values[0][2].strftime('%Y-%m-%d'))

    # retrieval of user data from the DB

    usersDf = pandas.read_sql(("SELECT * FROM user_newsletter "),newsletter_db)


    # LOOP on all users to test if they have at least 3 publications concerning them
    print()
    print()
    print()
    print("START OF THE PROCESS OF DETECTING USERS TO NOTIFY AND SEND MAILS")
    print()
    usersToNotify = []
    for user in usersDf.values :

    # treatment for one user
        userId = user[0]
        userName = user[1]
        userPhone = user[2]
        userEmail = user[3]
        userCategory =user[4]
        print()
        # detecting what are the categories that interest him
        userCategories =''
        if userCategory == '000':
            userCategories = "p.category = '000'"
        if userCategory == '001' :
            userCategories = " p.category ='001' or p.category = '111' "
        if userCategory == '010' :
            userCategories = " p.category ='010' or p.category = '111' "
        if userCategory == '100' :
            userCategories = " p.category ='100' or p.category = '111' "
        if userCategory == '011' :
            userCategories = " p.category ='001' or p.category ='010' or p.category = '111' "
        if userCategory == '101' :
            userCategories = " p.category ='001' or p.category ='100' or p.category = '111' "
        if userCategory == '110' :
            userCategories = " p.category ='100' or p.category ='010' or p.category = '111' "
        if userCategory == '111' :
            userCategories = " p.category ='001' or p.category ='010'or p.category ='100' or p.category = '111' "


        print('ID : ' + userId + ', NAME : ' + userName + ', CATEGORY : ' + userCategory + ';' )
        print(" CATEGORIES : " + userCategories)

        # we load all the publications that interest him and he never receive from the newsletter
        userPublicationsDf = pandas.read_sql(("SELECT * FROM publication as p WHERE ("+ userCategories +") and p.id not in ( SELECT news_id from flags where user_id = '"+ userId +"') ORDER BY creation_date "),newsletter_db)

        print("PUBLICATIONS THAT INTERESTS  "+ userName +" : " + str(userPublicationsDf.shape[0]))
        print(userPublicationsDf)

        # We check if there are at least 3 publications that interest him
        if( userPublicationsDf.shape[0] > 2 ):
            usersToNotify += [user]
            print("At least 3 publications so we send an email to : " + userName)
            publications = []
            # we collect the 3 oldest publications
            for i in range(0,3):
                publications.append(userPublicationsDf.values[i])

            # sending of the 3 publication to the user
            NS.send_newsletter(userName, userEmail, publications)

            # insertion of the 3 flags corresponding for the user and the 3 publications.
            for i in range (0,3):
                hash_object = hashlib.md5((userId + userPublicationsDf.values[i][0]).encode())
                id = hash_object.hexdigest()
                flagsArray = np.array([[id,userId,userPublicationsDf.values[i][0]]])
                flagsDf = pandas.DataFrame(flagsArray,
                                           columns=['id', 'user_id', 'news_id'])
                flagsDf.to_sql('flags', newsletter_db, if_exists='append', index=False)

    print("USERS NOTIFIED : ")
    for user in usersToNotify :
        print(user[1] +" : "+ user[2]+" , " + user[3] +" , " + user[4]+ " ; " )
