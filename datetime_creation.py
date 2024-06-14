import datetime


# Task 1. Using the variable called `current_datetime`, print out the current year
print('Task 1')
def task1():
    current_datetime = datetime.datetime.now()
    print(current_datetime.year)
task1()


# Task 2. Using the variable called `some_date`, print out the current day of the week
print('\nTask 2')
def task2():
    some_date = datetime.datetime.now()
    print(some_date.weekday() + 1)  # Adding 1 to get the index number of the weekday (1-7)
task2()


# Task 3. Write a Python program to determine whether the year 2021 is a leap year.
print('\nTask 3')
def task3():
    if datetime.datetime(2021, 1, 1).year % 4 == 0:   
        print('2021 is a leap year')
    else:
        print('2021 is not a leap year')
task3()


# Task 4. Convert a user provided string into a datetime object.
print('\nTask 4')
def task4():
    date_as_string = input("Please input the date and time you want to convert to a datetime object: ")
    date_object = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
    print(date_object)
task4()