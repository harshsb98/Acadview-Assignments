'''
#Q1
ime(sec)​ – This function returns a structure with 9 values each representing
a time attribute in sequence. It converts seconds into time attributes(days, years,
months etc.) till specified seconds from epoch. If no seconds are mentioned, time
is calculated till present. The structure attribute table is given below.This is time tuple
'''
#Q2
import datetime
import time
print(time.ctime())

#Q3 & Q4 & Q6
import datetime
import time
from datetime import date
from datetime import datetime
x=str(date.today())
x=datetime.strptime(x,"%Y-%m-%d")
print(x.month)
print(x.day)
print(x)
print(x.day)

#Q6
import time
print(time.localtime())

#Q7
import math
v=int(input("enter a number"))
print(math.factorial(v))

#Q8
import math
e=int(input("enter number 1"))
z=int(input("enter number 2"))
print(math.gcd(e,z))


#Q9
import os
print(os.getcwd())
print(os.environ)

