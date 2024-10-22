# -*- coding: utf-8 -*-
import time
from calendar import isleap
from datetime import datetime

def judge_leap_year(year):
    """Determine if a given year is a leap year."""
    return isleap(year)

def month_days(month, leap_year):
    """Return the number of days in a given month, accounting for leap years."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year else 28
    return 0  # Invalid month

def calculate_age(name, age):
    """Calculate and return the age in years, months, and days."""
    localtime = time.localtime()
    
    # Calculate the total months and days
    current_year = localtime.tm_year
    current_month = localtime.tm_mon
    current_day = localtime.tm_mday
    
    # Determine the birth year
    birth_year = current_year - age
    leap_year = judge_leap_year(current_year)

    # Calculate total days in age
    total_days = 0
    
    # Calculate days for full years
    for year in range(birth_year, current_year):
        total_days += 366 if judge_leap_year(year) else 365

    # Calculate days for the current year
    for month in range(1, current_month):
        total_days += month_days(month, leap_year)
    
    total_days += current_day  # Add current day's count

    # Calculate months
    total_months = age * 12 + (current_month - 1)

    return total_days, total_months

# Get user input
name = input("Input your name: ")
age = input("Input your age: ")

# Validate age input
try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative.")
except ValueError as e:
    print(f"Invalid input for age: {e}")
else:
    # Calculate age in days and months
    total_days, total_months = calculate_age(name, age)

    # Output the results
    print(f"{name}'s age is {age} years or {total_months} months or {total_days} days.")
