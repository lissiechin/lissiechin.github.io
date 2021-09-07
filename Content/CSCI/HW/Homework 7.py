##Lissie
## Hw 7: 10 & 12
## March 1, 2019


#10
def is_rightangled(a, b, c):
    if float(c**2) == float(a**2 + b**2):
        return True
    elif abs(float(c**2 -(a**2 + b**2))) < 0.001:
        return True
    return False
print(is_rightangled(12,34,100))


#12
def isLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            return False
        return True
    return False
y = isLeap(1985)
print(y)
z =isLeap (2000)
print(z)
user_put = int(input("enter a year"))
w = isLeap(user_put)
print(w)
                                                     

#write a program that asks for the month and year and prints the number of days in the month
month = str(input ("what is the month?"))                   #asking user
year = int(input ("what is the year?"))

def days_of_Month (month, year):
    if month in ['January', 'March', 'May', 'July', 'August', 'October', 'December']:
        return 31
    elif month in ['April', 'June',' September', 'November']:
        return 30
    elif month == 'February' and isLeap(year) == True:
        return 29
    elif month == 'February' and isLeap(year) == False:
        return 28
    return days_of_Month

print(days_of_Month(month,year))
        

# write a program that asks for the day and month of user's birthday and returns when they turn 100 (check against current month)

from datetime import date
import calendar
B_month = int(input("what month were you born? (1-12)"))
age = int(input("how old are you"))

def turn_100 (B_month, age):
      new_year = 2019 + (100-age)
      C_month = int(input("what is the current month?"))
      if (B_month >= C_month):
            return new_year -1 
      elif B_month < C_month:
            return new_year
      return turn_100

print(turn_100(B_month, age))
