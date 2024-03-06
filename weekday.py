# Write a program that outputs wether or not today is a weekday.

import datetime # import datetime module

weekno = datetime.datetime.today().weekday() #.today gets today's day, same with .weekday

if weekno < 5: # this will print the weekdays
    print ("Yes, unfortunately today is a weekday.")
else: # this will print the weekends
    print ("It is the weekend, yay!")


# reference: https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python