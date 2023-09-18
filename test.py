
def my_fun(*a):
    return lambda a, b, c : c + (b - a)

random = my_fun(0)

print(random(3, 2, 10))

print(10 + (2 - 3))


import time as tm

print(tm.ctime())
print(tm.localtime())
print(tm.gmtime())
tm.sleep(0)
print(tm.process_time())
print(tm.timezone)
print('\t' + '------------------------------------------------------------------------')

import datetime as dt

a = dt.datetime.today()

print(f"{a.day} {a.hour}/{a.minute}/{a.second}")
print('\v')

#Regex
#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab
#\w: same as (a-z, A-Z, 0-9 and _)
#\W: same as inverse of \w
#\s: (\f,\n,\r,\t,\v)

import re

email = "sk@aol.com md@.com @seo.com dc@com sk@aol.com kelvitz716@gmail.com"

print("ValidEmail:", len(re.findall("[\w._%+-]{1-20}@[\w.-]{2-20}.[A-Za-z]{2-3}",email)))


import matplotlib.pyplot as mplb


import pandas as pd

import numpy 
import scipy
import matplotlib.pyplot
import seaborn  
import cv2  


import datetime as dt
import time as tm

a = dt.date.today()
print(f"a: {a.day}/{a.month}/{a.year}: {a}")

#b = input('Enter due date: ')
b = tm.localtime()
print(f"b: {b}")

c = tm.ctime()
print(f"c: {c}")

e = tm.time()
print(f"e: {e}")

#f = input('datetime is: ')

d = tm.mktime(b)
print(f"d: {d}")

f = tm.asctime(b)
print(f"f: {f}")

g = tm.asctime((2023,9,8,14,33,22,0,0,0))
print(f'g: {g}')

h = tm.mktime((2023,9,8,14,33,22,0,0,0))
print(f"h: {h}")

i = h - d
print(f"i: {i}")

due_date = '28/02/1996'
j = tm.strptime(due_date, '%d/%m/%Y')
print(f"j: {j}")
print('\v')

today = dt.datetime.today()
print(f'today is: {today}')

some_year = 1997
some_month = 6
some_day = 7
that_day = dt.datetime(some_year,some_month,some_day)
print(f'some day is {that_day}')

day_difference = today - that_day
print(f'difference in days: {day_difference}')
print('\v')

dict1 = {'Name':'Kelvin', 'Age':20, 'Class':'Last'}
dict1['Age'] = 30
print(dict1['Age'])
s = str(dict1)
print(s) 
name = dict1.get('Name')
print(f"The Name is {name}")

import base64
str = "This is the actual text to be encoded and decoded"
str = base64.standard_b64encode(str.encode())
print(str)
str = base64.standard_b64decode(str.decode())
print(str)
print('\v')

aTuple = (123,"java", 3.23)
list1 = list(aTuple)
list1.append()







