"""
Take a year as input. Check if it is a leap year. A year is a leap
year if it is divisible by 4, but not by 100, unless it is also
divisible by 400.

200 - not a leap year
204 - leap

800 - leap year
"""

year = int(input("Enter the Year:"))
if year % 4 == 0 and year % 100 != 0:
    if year % 400 == 0:
        print("Leap year")
else:
    print("Not Leap year")
