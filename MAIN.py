import NEWS_EXTRACTOR
import PUBLICATION_EXTRACTOR
import PRESSRELEASE_EXTRACTOR
import TRIGGERING_NEWSLETTER
import PREVIEW_NEWSLETTER
import time
from _datetime import datetime


correct = False
while(not(correct)):
    print("Please enter the start date for the scrawling : ( FORMAT : YYYY-MM-DD )")
    startdate = input()
    if(len(startdate) == 10):
        if(startdate[0] in '0123456789' and startdate[1] in '0123456789' and startdate[2] in '0123456789' and startdate[3] in '0123456789' and startdate[5] in '0123456789' and startdate[6] in '0123456789' and startdate[8] in '0123456789' and startdate[9] in '0123456789' and startdate[0] in '0123456789' and startdate[4] == '-' and startdate[7] == '-'):
            correct = True


correct = False
while(not(correct)):
    print("Please enter the end date for the scrawling : ( FORMAT : YYYY-MM-DD)")
    enddate = input()
    if(len(enddate) == 10):
        if(enddate[0] in '0123456789' and enddate[1] in '0123456789' and enddate[2] in '0123456789' and enddate[3] in '0123456789' and enddate[5] in '0123456789' and enddate[6] in '0123456789' and enddate[8] in '0123456789' and enddate[9] in '0123456789' and enddate[0] in '0123456789' and enddate[4] == '-' and enddate[7] == '-'):
            correct = True

print('START : '+ startdate)
print('END : '+ enddate)

# EXTRATION OF THE NEW ARTICLE FROM THE 3 WEB PAGES OF BPS
NEWS_EXTRACTOR.extract_news(datetime.strptime(startdate, '%Y-%m-%d'),datetime.strptime(enddate, '%Y-%m-%d'))
PUBLICATION_EXTRACTOR.publication_extract(datetime.strptime(startdate, '%Y-%m-%d'),datetime.strptime(enddate, '%Y-%m-%d'))
PRESSRELEASE_EXTRACTOR.pressrelease_extract(datetime.strptime(startdate, '%Y-%m-%d'),datetime.strptime(enddate, '%Y-%m-%d'))

#SENDING TO YOUR MAIL A PREVIEW TO SEE IF YOU ARE OKAY TO SEND IT
PREVIEW_NEWSLETTER.preview_by_mail()

# FINDING USERS TO NOTIFY AND THEN SEND EMAIL
print('A PREVIEW OF THE NEWSLETTER OF ALL THE CATEGORIES HAS BEEN SEND TO THE TEST MAIL PLEASE CHECK IT BEFORE SEND TO THE USERS !')
print()
print()
print('DO YOU WANT TO SEND THE NEWSLETTERS TO THE USERS ? (please enter 1 for YES or 2 for NO)')
send = input()
if(send == '1'):
    TRIGGERING_NEWSLETTER.trigger_and_mail()
else :
    print("THE NEWSLETTERS HAS NOT BEEN SEND ! ")