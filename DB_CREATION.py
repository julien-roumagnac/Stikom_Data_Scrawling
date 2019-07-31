from sqlalchemy import create_engine
import hashlib
#import unicodedata
import pandas
import numpy as np
import sys
import time
from datetime import datetime

db_string = 'postgres://gposlylgjnslfm:7a234bb7261fc07a69167f7a367a158c9f556b902b46aa2cea0c4aecc2c25302@ec2-107-22-211-248.compute-1.amazonaws.com:5432/d690d9feoboig0'

#db_string = 'postgres://admin:admin@localhost:5432/newsletter'

engines = [create_engine(db_string)]
def createDatabase():
    for db in engines:
        db.execute("DROP TABLE IF EXISTS user_newsletter")
        db.execute("DROP TABLE IF EXISTS flags")
        db.execute("DROP TABLE IF EXISTS publication")
        db.execute("CREATE TABLE publication (id varchar(50) NOT NULL, publication_text text,creation_date timestamp, imgelink varchar(500), category varchar(5), title varchar(250), full_link varchar(500), download_link varchar(500))")
        db.execute("CREATE TABLE user_newsletter (id varchar(50) NOT NULL, username varchar(100) NOT NULL,phonenumber varchar(50), email varchar(100) NOT NULL, prefbroadcast varchar(5), sex varchar(2), company varchar(100), home_address varchar(500),occupation varchar(100), knowing_bps_from varchar(100),survey_respondent varchar(100),creation_date timestamp)")
        db.execute("CREATE TABLE flags (id varchar(50) NOT NULL, user_id varchar(100) NOT NULL ,news_id varchar(100) NOT NULL)")

        userArray = np.array([[1, 'TestUser', '+628123456789', 'gianyarkab.newsletter@gmail.com', '001', '0', 'CompanyXXX', 'Stikom bali denpasar 5432 oo Baz','Student','Social Media','1','2019-01-01']])
        userDf = pandas.DataFrame(userArray,
                                  columns=['id', 'username', 'phonenumber', 'email', 'prefbroadcast', 'sex',
                                           'company', 'home_address','occupation','knowing_bps_from','survey_respondent','creation_date'])
        userDf.to_sql('user_newsletter', db, if_exists='append', index=False)

def main():
    createDatabase()
    print("done")

if __name__ == "__main__":
  #Run as main program
  main()