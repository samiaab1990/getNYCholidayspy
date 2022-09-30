from getNYCholidayspy import getnycholidays

# gets data frame 
print(getnycholidays.dataframe)

# gets dates only
print(getnycholidays.dates)

# gets date from keyword
print(getnycholidays.holidaydate(holiday_keyword = "New Years"))

# gets holiday date from date
print(getnycholidays.holidaydate(date_keyword = "2022-01-01"))

# gets holiday date from weekday
print(getnycholidays.holidaydate(weekday="Monday"))

# returns day of week from keyword
print(getnycholidays.returnday(holiday_keyword = "New Years"))

# returns day of week from date
print(getnycholidays.returnday(date_keyword = "2022-01-01"))

# returns day of week from weekday
print(getnycholidays.returndaye(weekday="Monday"))
