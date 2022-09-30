# getNYCholidayspy
A Python version of the getNYCholidays package. Retrieves a vector of official NYC holiday dates from the NYC Office of Payroll Administration's List of Holidays PDF. Allows to retrieve dates by filtering on holiday name, weekday and date.

<!-- badges: start -->
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/samiaab1990/getNYCholidayspy)

<!-- badges: end -->

Retrieves a vector of New York City holidays dates as listed on the NYC Office of Payroll Administration's List of Holidays PDF in R. 

## Installation

You can install the development version of getNYCholidays from [GitHub](https://github.com/) with:

``` python 
pip install git+https://github.com/samiaab1990/getNYCholidayspy.git#egg=getNYCholidayspy
```

## Example
```python
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
```
