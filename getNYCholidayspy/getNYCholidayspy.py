import datetime
import pandas as pd
import numpy as np
import pdfplumber
import string
import re
import requests
import io
from requests.api import get



year = str(datetime.date.today().year)
url = 'https://www1.nyc.gov/assets/opa/downloads/pdf/'+year+'-list-of-holidays.pdf'
response = requests.get(url)
pdf_data = io.BytesIO(response.content)
contents =  pdfplumber.open(pdf_data)
text = contents.pages[0].extract_text().split('\n')
dates = text[2:len(text)-1]
headers = text[1].split(' ')

reg_month_day = re.compile('(?P<month>[a-zA-Z\.\*]+)\s+(?P<day>\d{1,2})')
reg_year = re.compile('(?P<year>\d{4})')
reg_holiday_label = re.compile('(?P<label>[^\d+]+$)')

date_list=[]
holiday_list =[]

for i in dates:
    i = re.sub(r'[^\w\s]','',i)
    md = reg_month_day.search(i)
    y = reg_year.search(i)
    holiday = reg_holiday_label.search(i)
    holiday_list.append(holiday.group('label').lstrip())

    if y == None:
        date_list.append(md.group('month')+' '+md.group('day')+', '+year)
    else:
        date_list.append(md.group('month')+' '+md.group('day')+', '+y.group('year'))
    

def date_time_parser(input_date):
    for format in ('%B %d, %Y', '%b %d, %Y'):
        try:
            return datetime.datetime.strptime(input_date,format)
        except ValueError:
            pass
        

yyyymmdd = []
day_of_week = []

for date in date_list:
    yyyymmdd.append(date_time_parser(date))
for date in yyyymmdd:
    day_of_week.append(date.strftime('%A'))

d = {'Dates':date_list,'Holidays':holiday_list, 'yyyy.mm.dd':yyyymmdd, 'day_of_week':day_of_week}

holidays_data_frame = pd.DataFrame(d)

class getnycholidays:
    dataframe = holidays_data_frame
    dates = holidays_data_frame['yyyy.mm.dd']
    
    def __init__(self,holiday_keyword=None,date=None,date_keyword=None, weekday=None):
        self.holiday_keyword = holiday_keyword
        self.date = date
        self.date_keyword = date_keyword
        self.weekday = weekday
    
    def holidaydate(holiday_keyword=None,date_keyword=None, weekday=None):
        if holiday_keyword != None:
            return holidays_data_frame[holidays_data_frame['Holidays'].str.contains(holiday_keyword, case=False)][['yyyy.mm.dd','Holidays']]
        elif date_keyword != None:
            return holidays_data_frame[holidays_data_frame['Dates'].str.contains(date_keyword, case=False)][['yyyy.mm.dd','Holidays']]
        elif weekday != None:
            return holidays_data_frame[holidays_data_frame['day_of_week'].str.contains(weekday, case=False)][['yyyy.mm.dd','Holidays']]
        else:
            print("Not Applicable")
    def returnday(holiday_keyword = None, date_keyword = None, date = None):
        if holiday_keyword !=None:
            return holidays_data_frame[holidays_data_frame['Holidays'].str.contains(holiday_keyword, case=False)][['day_of_week','yyyy.mm.dd','Holidays']]
        elif date_keyword !=None:
            return holidays_data_frame[holidays_data_frame['Dates'].str.contains(date_keyword, case=False)][['day_of_week','yyyy.mm.dd','Holidays']]
        elif date!=None:
            return holidays_data_frame[holidays_data_frame['yyyy.mm.dd'] == pd.to_datetime(date)][['day_of_week','Holidays']]
        else:
            print("Not Applicable")
        
        





 
        






