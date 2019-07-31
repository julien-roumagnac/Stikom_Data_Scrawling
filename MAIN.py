import NEWS_EXTRACTOR
import PUBLICATION_EXTRACTOR
import PRESSRELEASE_EXTRACTOR
import TRIGGERING_NEWSLETTER
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

# FINDING USERS TO NOTIFY AND THEN SEND EMAIL
TRIGGERING_NEWSLETTER.trigger_and_mail()
