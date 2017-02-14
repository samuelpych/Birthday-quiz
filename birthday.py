"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
name=input("what is your name? ")
month=input("Hi " +name+ " what month are you born in? ")
year= input ("What year are you born in? ")
day= input("What day are you born on? ")
february=int(2)
january=int(1)
march=int(3)
june=int(6)
july=int(7)
august=int(8)
april=int(4)
september=int(9)
october=int(10)
november=int(11)
may=int(5)
december=int(12)
if todaymonth == [december, january, february]:
    todaymonth=winter
elif todaymonth == [3, 4, 5]:
    todaymonth = spring
elif todaymonth == [6, 7, 8]:
    todaymonth = summer
elif todaymonth == [9, 10, 11]:
    todaymonth = fall
if todaymonth == [december, january, february] and year >=1990 and year <=1999:
    print(+name+ "you are a winter baby of the 90's")
elif todaymonth == [december, january, february] and year >=1980 and year <=1989:
    print(+name+ "you are a winter baby of the 80's")
elif todaymonth == [december, january, february] and year <1980:
    print(+name+ "you are a winter baby of the stone age")
elif todaymonth == [december, january, february] and year >=2000 and year <=2009:
    print(+name+ "you are a winter baby of the 2000's")
if todaymonth == [march, april, may] and year >=1990 and year <=1999:
    print(+name+ "you are a spring baby of the 90's")
elif todaymonth == [march, april, may] and year >=1980 and year <=1989:
    print(+name+ "you are a spring baby of the 80's")
elif todaymonth == [march, april, may] and year <1980:
    print(+name+ "you are a spring baby of the stone age")
elif todaymonth == [march, april, may] and year >=2000 and year <=2009:
    print(+name+ "you are a spring baby of the 2000's")
if todaymonth == [june, july, august] and year >=1990 and year <=1999:
    print(+name+ "you are a summer baby of the 90's")
elif todaymonth == [june, july, august] and year >=1980 and year <=1989:
    print(+name+ "you are a summer baby of the 80's")
elif todaymonth == [june, july, august] and year <1980:
    print(+name+ "you are a summer baby of the stone age")
elif todaymonth == [june, july, august] and year >=2000 and year <=2009:
    print(+name+ "you are a summer baby of the 2000's")
if todaymonth == [september, october, november] and year >=1990 and year <=1999:
    print(+name+ "you are a fall baby of the 90's")
elif todaymonth == [september, october, november] and year >=1980 and year <=1989:
    print(+name+ "you are a fall baby of the 80's")
elif todaymonth == [september, october, november] and year <1980:
    print(+name+ "you are a fall baby of the stone age")
elif todaymonth == [september, october, november] and year >=2000 and year <=2009:
    print(+name+ "you are a fall baby of the 2000's")
    

