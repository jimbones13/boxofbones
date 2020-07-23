# This program will calculate the day of the week for any given day.

##########################################################################
# Input Function

# Purpose: Collect information
# Arguments: 
# Result: (month,day,year)

# Avoid Globals

def date_info():
	month = input("\nWhat is the month for your date? ").lower()
	day = int(input("\nWhat is the day of the month? "))
	year = int(input("\nWhat is the year? "))
	return (month,day,year)

#(month,day,year) = date_info()

#print(month)
#print(day)
#print(year)

##########################################################################
# Number of days in month - DID NOT END UP USING THIS FUNCTION

# Purpose: Given the month, returns the number of days in the month
# Arguments: month
#						year
# Result: Number of Days in the month
# Could be used as a list

def days_in_month(month,year):
    if month == 'january':
        return 31
    elif month == 'february' and leap_year(year) == False:
        return 28
    elif month == 'february' and leap_year(year) == True:
        return 29
    elif month == 'march':
        return 31
    elif month == 'april':
        return 30
    elif month == 'may':
        return 31
    elif month == 'june':
        return 30
    elif month == 'july':
        return 31
    elif month == 'august':
        return 31
    elif month == 'september':
        return 30
    elif month == 'october':
        return 31
    elif month == 'november':
        return 30
    elif month == 'december':
        return 31

#print("testing days in september: ", days_in_month('september'), "should be 30")

##########################################################################
# Number of days in year prior to that month

# Purpose: Given the month, returns the sum of days in the months prior
# Arguments: month
# Result: Total number of days prior to the month
# Could be created using recursion and the function right before this one. Als

def days_before_month(month):
    if month == 'january':
        return 0
    elif month =='february':
        return 31
    elif month == 'march':
        return 31 + 28
    elif month == 'april':
        return 31 + 28 + 31
    elif month == 'may':
        return 31 + 28 + 31 + 30
    elif month == 'june':
        return 31 + 28 + 31 + 30 + 31
    elif month == 'july':
        return 31 + 28 + 31 + 30 + 31 + 30
    elif month == 'august':
        return 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month == 'september':
        return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month == 'october':
        return 273
    elif month == 'november':
        return 304
    elif month == 'december':
        return 334

#print("testing days before August in a leap year: ", days_before_month('august',True), "should be 213")
#print("testing days before June in a non-leap year: ", days_before_month('june',False), "should be 151")

##########################################################################
# Is the given year a leap year

# Purpose: Identifies if the given year is a leap year
# Arguments: year
# Result: True it if's a leap year, False if it is not a leap year

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False

#print("testing if 1800 is a leap year: ", leap_year(1800), "should be False")
#print("testing if 1925 is a leap year: ", leap_year(1925), "should be False")
#print("testing if 2012 is a leap year: ", leap_year(2012), "should be True")
#print("testing if 2400 is a leap year: ", leap_year(2400), "should be True")

##########################################################################
# Number of leap years between 1752 and given year

# Purpose: Determines number of leap years between 1752 and given year
# Arguments: year
# Result: Number of leap years.
# Comment: I think there is a way to write this as an actual math function rather than a series of ifs

def number_of_leapyears(year):
    number_of_years = year - 1752
    possible_leapyears = number_of_years // 4
    if year >= 2600:
        return possible_leapyears - 7
    elif year >= 2500:
        return possible_leapyears - 6
    elif year >= 2300:
        return possible_leapyears - 5
    elif year >= 2200:
        return possible_leapyears - 4
    elif year >= 2100:
        return possible_leapyears - 3
    elif year >= 1900:
        return possible_leapyears - 2
    elif year >= 1800:
        return possible_leapyears - 1
    else:
        return possible_leapyears

#def number_of_leapyears2(year):
#  return (year - 1752) // 4 - (year - 1700) // 100 + (year - 1600) // 400

#print("testing how many leap years occur between 1752 and 1752: ", number_of_leapyears(1752), "should be 0")
#print("testing how many leap years occur between 1752 and 1968: ", number_of_leapyears(1968), "should be 26")
#print("testing how many leap years occur between 1752 and 2375: ", number_of_leapyears(2375), "should be 150")
#print(f"testing how many leap years occur between 1752 and {year}: {number_of_leapyears(year)} should be 84")

##########################################################################
# Number of Days Function

# Purpose: Converts a date, in the form "Month, Day, Year" into number of days since Sept 14, 1752
# Arguments: Month
#            Day
#            Year
# Result: Number of Days
# 108 is remaining days in 1752

def total_days(month,day,year):
    if year != 1752:
        if leap_year(year) == True:
            if month == 'february':
                return 108 + 365 * year - 1753 + int(number_of_leapyears(year)) + int(days_before_month(month)) + int(day) - 1
            elif month == 'january':
                return 108 + 365 * year - 1753 + int(number_of_leapyears(year)) + int(days_before_month(month)) + int(day) - 1
            else:
                return 108 + 365 * year - 1753 + int(number_of_leapyears(year)) + int(days_before_month(month)) + int(day)
        else:
            return 108 + 365 * int(year - 1753) + int(number_of_leapyears(year)) + int(days_before_month(month)) + int(day)
    else:
        return int(days_before_month(month)) - int(days_before_month('september')) + int(day) - 14
        
# Remove ints

#print("testing the total days since 10/1/1752: ", total_days('october',1,1752), "should be 17")
#print("testing the total days since 1/13/1753: ", total_days('january',13,1753), "should be 121")
#print("testing the total days since 6/28/1963: ", total_days('june',28,1963), "should be 76987")
#print("testing the total days since 4/17/2009: ", total_days('april',17,2009), "should be 93717")

##########################################################################
# Calculate the remainder after dividing number of days by 7

# Purpose: Finds the remainder after dividing total days by 7 - Starting with Thursday
# Arguments: total_days
# Result: Day of week

def day_of_week(total_days):
	weekday_number = total_days % 7
	if weekday_number == 0:
		return 'Thursday'
	elif weekday_number == 1:
		return 'Friday'
	elif weekday_number == 2:
		return 'Saturday'
	elif weekday_number == 3:
		return 'Sunday'
	elif weekday_number == 4:
		return 'Monday'
	elif weekday_number == 5:
		return 'Tuesday'
	else:
		return 'Wednesday'
		
#print("testing what day of the week : ", day_of_week(23), "should be Saturday")
#print("testing what day of the week : ", day_of_week(35), "should be Thursday")
#print("testing what day of the week : ", day_of_week(165), "should be Monday")
#print("testing what day of the week : ", day_of_week(13), "should be Wednesday")

##########################################################################
# Weekday Function

# Purpose: Converts a date, in the form "Month, Day, Year" into the day of the week.
# Arguments: Month
#			 Day
#			 Year
# Result: Day of the week (Sunday, Monday, Tuesday, etc.)

def weekday(month,day,year):
	return day_of_week(total_days(month,day,year))


print("testing 12/13/1989: ", weekday('december',13,1989), "should be a something")
print("testing 5/16/2004: ", weekday('may',16,2004), "should be a Sunday")
print("testing 8/26/2135: ", weekday('august',26,2135), "should be a Friday")
print("testing 5/1/1845: ", weekday('may',1,1845), "should be a Thursday")
print("testing 8/11/1996: ", weekday('august',11,1996), "should be a Sunday")
print("testing 7/4/1776: ", weekday('july',4,1776), "should be a Thursday")
print("testing 12/13/2400: ", weekday('december',13,2400), "should be a Wednesday")
print("testing 1/6/2236: ", weekday('january',6,2236), "should be a Wednesday")
print("testing 5/15/1987: ", weekday('may',15,1987), "should be a Friday")


##########################################################################
# Run the program

#print("\nEnter a date, and the program will tell you what day of the week it is.\n")
#date_info()
#print(f"\nThe date {month.title()} {day}, {year} will occurr, or has occurred, on a {weekday(month,day,year)}.")



