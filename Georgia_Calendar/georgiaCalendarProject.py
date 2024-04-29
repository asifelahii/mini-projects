# Project 01 - Calendar
"""This script generates a calendar for a given year and
    displays it in the console."""

import datetime

def firstDayOfAYear(year):
    """
    Determines the day of the week for the first day of the year.

    Parameters:
    year (int): The year for which the first day of the year is to be determined.

    Returns:
    int: The index of the day of the week (0 for Sunday, 1 for Monday, etc.) for the first day of the year.
    """
    day = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
    a = datetime.date(year, 1, 1).weekday() + 1  # Adding 1 because the tuple starts from Sunday.
    return a

# Drive Code

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
day = ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
dayInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# variables for:
weekday = 0
spaceCounter = 0
totalDays = 0

year = int(input("Enter your favorite year: "))

print("\n***************", end=" ")
print("Welcome to ", year, end=" ")
print("***************\n",)

# Checking for leap year
if (year % 4 == 0 or year % 400 == 0) and year % 100 != 0:
    dayInMonth[1] = 29

# Get the index of the first day of the year
weekday = firstDayOfAYear(year)

# Printing the calendar
for i in month:
    print("\n-------------------", end=" ")
    print(i, end=" ")  # Printing name of months.
    print("-------------------\n")

    # Printing name of weekdays.
    for j in day:
        print(j, end="    ")
    print("\n")
    
    # Printing leading spaces to align the first day of the month with its corresponding weekday.
    for s in range(weekday):
        print("       ", end="")
    
    # Printing days between [1-31]
    for k in range(len(dayInMonth)):
        if month[k] == i:
            for l in range(dayInMonth[k]):
                # Printing each day with proper spacing and formatting
                if l + 1 > 9:
                    print(l + 1, "    ", end="")
                else:
                    print("", l + 1, "    ", end="")
                
                # Incrementing weekday counter and handling line breaks for the next week
                weekday += 1
                if weekday > 6:
                    weekday = 0
                    print("\n")        
            print("\n\n")