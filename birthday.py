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
name=input("what is your name? ")
month=input("Hi " +name+ " what month are you born in? ")
year= input ("What year are you born in? ")
day= input("What day are you born on? ")
if month in ["January", "February", "December"] and year <2000 and year >1989:
    print("Hi " +name+ "you are a winter baby of the 90's")
if month in ["March", "April", "May"] <2000 and year >1989:
    print("Hi " +name+ "you are a spring baby of the 90's")
if month in ["June", "July", "August"] and year <2000 and year >1989: 
    print("Hi " +name+ "you are a summer baby of the 90's")
if month in ["September", "October", "November"] and year <2000 and year >1989: 
    print("Hi " +name+ "you are a fall baby of the 90's")
