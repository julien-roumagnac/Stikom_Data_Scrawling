# coding: utf-8

from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import pandas
import numpy as np
import requests
import hashlib
import time
from datetime import datetime

newsletter_db = create_engine('postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0')

usersDf = pandas.read_sql(("SELECT * FROM user_newsletter order by creation_date "),newsletter_db)
print('ALL USERS ALLREADY INSERTED ORDER BY DATE')
print()
for user in usersDf.values :
    print("ID : "+user[0]+" "+user[1]+" : "+user[3]+", "+user[4]+";")

print()






insert = '2'
while(insert =='2'):
    print(" Hello this file help you to add a new user in the Database of the BPS newsletter ! ")

    print(" Please enter the USERNAME : ")
    username = input()
    print("username : ", username)
    print()

    print(" Enter his phone number : ")
    phonenumber = input()
    print("phonenumber : ", phonenumber)
    print()

    print(" Enter his email" )
    email = input()
    print("email : ", email)
    print()

    correct = False
    while(not(correct)):
        print(" Enter his favorites broadcast '001' for X '100' for Y '010' for Z or '111' for XYZ ")
        prefbroadcast = input()
        if(len(prefbroadcast) == 3):
            if(prefbroadcast[0] in '01' and prefbroadcast[1] in '01' and prefbroadcast[2] in '01'):
                correct = True


    print("prefbroadcast : ", prefbroadcast)
    print()

    correct = False
    while(not(correct)):
        print(" Enter the sex of the user '1' for man '2' for woman ")
        sex = input()
        if (len(sex) == 1):
            if (sex[0] in '12' ):
                correct = True
    print("sex : ", sex)
    print()

    print(" Enter his company ")
    company = input()
    print("company : ", company)
    print()

    print(" Enter his full address")
    addres = input()
    print("address : ", addres)
    print()

    print(" Enter his occupation")
    occupation = input()
    print("occupation : ", occupation)
    print()

    print( "Enter where he is knowing BPS from ")
    kbps = input()
    print("kbps : ", kbps)
    print()

    print(" Enter if it's a survey respondent ")
    survey = input()
    print("survey : ", survey)

    date = datetime.today().strftime('%Y-%m-%d')


    print()
    print(" HERE IS ALL THE INFORMATION YOU JUST ENTER : ")
    print()
    print("username : ", username)
    print("phonenumber : ", phonenumber)
    print("email : ", email)
    print("prefbroadcast : ", prefbroadcast)
    print("sex : ", sex)
    print("company : ", company)
    print("address : ", addres)
    print("occupation : ", occupation)
    print("kbps : ", kbps)
    print("survey : ", survey)
    print()
    print("date : ",time.strftime(date))

    print("Do you want to insert this user or retry ?")
    correct = False
    while(not(correct)):
        print("INSERT : enter '1' or RETRY : '2'")
        insert = input()
        if (len(insert) == 1):
            if (insert[0] in '12' ):
                correct = True
    hash_object = hashlib.md5((email).encode())
    id = hash_object.hexdigest()
    if(insert =='1'):
        userArray = np.array([[id[:20], username, phonenumber, email, prefbroadcast, sex,
                               company, addres, occupation, kbps, survey,time.strftime(date)]])
        userDf = pandas.DataFrame(userArray,
                                  columns=['id', 'username', 'phonenumber', 'email', 'prefbroadcast', 'sex',
                                           'company', 'home_address', 'occupation', 'knowing_bps_from',
                                           'survey_respondent','creation_date'])
        userDf.to_sql('user_newsletter', newsletter_db, if_exists='append', index=False)
        print('USER INSERTED')
