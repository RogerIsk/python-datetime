import datetime as dt

# Task 1. Using the variable called `current_datetime`, subtract 15 days from the current time.
# Hint: use `.strftime()` method to reformat the time
print("Task 1")
current_datetime = dt.datetime.now()                    # Get the current time
new_datetime = current_datetime - dt.timedelta(days=15) # Go back 15 days / subtract 15 days from the current time
result = new_datetime.strftime("%Y-%m-%d")              # Reformat the time meaning we will show only the year, month and day
print(result)



# Task 2. Using the variable called `current_datetime`, add 7 days to the current time.
print("\nTask 2")
current_datetime = dt.datetime.now()                    # Get the current time
new_datetime = current_datetime + dt.timedelta(days=7)  # Add 7 days to the current time
result = new_datetime.strftime("%Y-%m-%d")              # Reformat the time meaning we will show only the year, month and day
print(result)



# Task 3. write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. 
# Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.
print("\nTask 3")
reminder_date = dt.datetime(2020, 1, 1) + dt.timedelta(days=25) # creating a datetime of the current date, January 1st, 2020 and adding 25 days to it
customer_name = "Friedrich"
message = f"Dear {customer_name}, please remember to pay your bill by {reminder_date.strftime('%Y-%m-%d')}. Thank you!"
print(message)