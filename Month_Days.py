import calendar
import time

#Check For Leap year

def leap_year(year):
    if calendar.isleap(year):
        return True
    else:
        return False


#Return the Number of days in months

def days_month(month,leap_year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11 :
        return 30
    elif month == 2 and leap_year:
        return 29
    elif month == 2 and (not leap_year):
        return 28


name = input("Enter Your Name : ")
age = int(input("Enter your age : "))
localtime = time.localtime(time.time())   
year = int(age)
month = year * 12 + localtime.tm_mon
day = 0

begin_year = int(localtime.tm_year) - year
end_year = begin_year + year

# calculate the days
for y in range(begin_year, end_year):
    if (leap_year(y)):
        day = day + 366
    else:
        day = day + 365

leap_year = leap_year(localtime.tm_year)
for m in range(1, localtime.tm_mon):
    day = day + days_month(m, leap_year)

day = day + localtime.tm_mday
print("%s's age is %d years or " % (name, year), end="")
print("%d months or %d days" % (month, day))
