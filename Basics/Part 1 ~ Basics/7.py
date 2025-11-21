'''
Write a program that reads hours, minutes and seconds separately and prints them on one line. 
Hours and minutes are integer numbers, seconds have 2 decimal places. 
Example: hours: 10 
         minutes: 11 
         seconds: 22.34 
         Time is 10 hours, 11 minutes and 22.34 seconds
'''

hrs = int(input("Give the hour: "))
min = int(input("Give the minutes: "))
sec = float(input("Give the seconds: "))

print(f"The time is {hrs} hours, {min} minutes and {sec} seconds")