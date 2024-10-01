# todo-1: Write a program that returns True or False whether if a given year is a leap year.

# todo: A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating

# todo This is how you work out whether if a particular year is a leap year.

# todo - on every year that is divisible by 4 with no remainder

# todo - except every year that is evenly divisible by 100 with no remainder

# todo - unless the year is also divisible by 400 with no remainder

# a function that takes a year
def is_leap_year(year):
    if year == "":
        return"The year is empty"
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(is_leap_year(2000))