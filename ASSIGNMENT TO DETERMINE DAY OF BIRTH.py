
"""
NAME: NABUUMA OLIVIA PEACE
COURSE:BSC BIOMEDICAL ENGINEERING
REG NO: 16/U/8238/PS
"""

import calendar
print("This Program is intended to determine the exact day of the week you were born")
print(".....................................................")
day = month = year = None
#Next code ensures that only and only integers input

while(day == None):
    try:
        day = int(input("PLEASE TYPE IN YOUR DAY OF YOUR BIRTH:"))
        while(day not in range(1, 32)):
            print("this is not a day")
            day = int(input("PLEASE TYPE IN YOUR DAY OF BIRTH:"))

    except:
        print("Please type in numbers only")
        print()

while(month == None):
    try:
        month = int(input("PLEASE TYPE IN YOUR MONTH OF BIRTH:"))
        while(month not in range(1, 13)):
            print("Mr or Lady, months move from Jan, To December. thats twelve, not %d or whatever you've input" % month)
            month = int(input("PLEASE TYPE IN YOUR MONTH OF BIRTH  AGAIN: "))

    except:
        print("Please type in numbers only")
        print()

while(year == None):
    try:
        year = int(input("PLEASE TYPE IN YOUR YEAR OF BIRTH: "))
        while(year not in range(1000, 2500)):
            if(year >= 2500):
                print("No offense but by %d, you'll be dead, ALREADY. So please, type in " % year)
                year = int(input("PLEASE TYPE IN YOUR YEAR OF BIRTH "))
            if(year < 1000):
                print("By then you were not born. Unless you are immortal")
                year = int(input("PLEASE TYPE IN YOUR YEAR OF BIRTH: "))

    except:
        print("Please type in numbers only")
        print()

#this outputs the day in form of numbers from 0 - 6
date = calendar.weekday(year, month, day)
exact = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("You were born on ", exact[date])


input("press Enter to exit")

