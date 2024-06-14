from calendar import monthrange
import calendar
import datetime
import os

clear = lambda: os.system('clear')
clear()

# Task 1. Write a Python script to display the various Date Time formats.
# Note: The output of the following Tasks can change according to when the program will be executed.**
# - Current date and time
# - Current year
# - Month of year
# - Week number of the year
# - Weekday of the week
# - Day of year
# - Day of the month
# - Day of week

print('\nTask 1')
print("Current date and time: ", datetime.datetime.now())
print("Current year: ", datetime.datetime.now().year)
print("Month of year: ", datetime.datetime.now().month)
print("Week number of the year: ", datetime.datetime.now().strftime("%U"))
print("Weekday of the week: ", datetime.datetime.now().strftime("%A"))
print("Day of year: ", datetime.datetime.now().strftime("%j"))
print("Day of the month: ", datetime.datetime.now().strftime("%d"))
print("Day of week: ", datetime.datetime.now().strftime("%A"))



# Task 2. Write a Python program to print yesterday, today, tomorrow. 

print('\nTask 2')
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1) # -1 day for yesterday
tomorrow = today + datetime.timedelta(days=1)  # +1 day for tomorrow
print("Yesterday: ", yesterday)
print("Today: ", today)
print("Tomorrow: ", tomorrow)



#Task 3. Write a Python program to add 5 seconds to the current time.
# **Hint:** you can use `timedelta` to solve the task.

print('\nTask 3')
current_time = datetime.datetime.now()
print("Current time:", current_time)
current_time = current_time + datetime.timedelta(seconds=5)
print("After adding 5 seconds:", current_time)



# Task 4. Write a Python program to print the next 5 days starting today. 
# **Hint:** you can use `timedelta` and `for` loop to solve the task.

print('\nTask 4')
today = datetime.datetime.now()
print("Today:", today)
print("Next 5 days:")
for i in range(1, 6):
    print(today + datetime.timedelta(days=i))



# Task 5. Write a Python program to convert Year/Month/Day to Day of Year using datetime module.

print('\nTask 5')
date = datetime.datetime.now()
print("Today:", date)
print("Day of the year:", date.strftime("%j"))



# Task 6. Write a Python program to find the date of the first Monday of a given week.

print('\nTask 6')
week = 34
year = 2023
first_day_of_week = datetime.datetime.strptime(f'{year}-W{week}-1', "%Y-W%W-%w")
print(f"The first Monday of this week was: {first_day_of_week.date()}")



# Task 7. Write a Python program to select all the Sundays in a specified year.
# **Hint:** Think about using a loop

print('\nTask 7')
year = input("Enter the year: ")
while not year.isdigit():                  # Check if the input is a real number
    year = input("Enter a proper year: ")  # If not, ask again
year = int(year)                           # Convert the input to an integer         
date = datetime.datetime(int(year), 1, 1)  # so we can use it in the datetime module
while date.year == year:                   # Loop until the year changes
    if date.weekday() == 6:                # 6 is Sunday
        print(date.date(), end=", ")       # Print the date when it's Sunday
    date += datetime.timedelta(days=1)     # Move to the next day after Sunday



# Task 8. Write a Python program to get the number of days in a given month and year.
# **Hint:** you can use `from calendar import monthrange`

print('\n\nTask 8')
year = 2023
month = 3
num_days = monthrange(year, month)[1]
print(f"Number of days in march is: {num_days}")



# TASK 9-BONUS TASK. Write a Python program to display a simple, formatted calendar of a given year and month.
# **Hint:** Use the `calendar` module to generate the calendar.

print('\n\nTask 9')
year = 2023
month = 3
print(calendar.month(year, month))