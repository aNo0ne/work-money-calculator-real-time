import time
import os

# Function to calculate the time difference in seconds
def get_time_diff(start_time, current_time):
    start_secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time.split(':'))))
    current_secs = sum(int(x) * 60 ** i for i, x in enumerate(reversed(current_time.split(':'))))
    return current_secs - start_secs

# Function to calculate the money made
def calculate_money(time_diff, price_per_hour, break_time):
    work_time = time_diff - break_time
    work_money = (work_time / 3600) * price_per_hour
    return work_money

# Get starting time and price per hour from the user
start_time = input("Enter the starting time in hh:mm:ss format: ")
price_per_hour = float(input("Enter the price per hour: "))

# Ask if the user was on a break
on_break = input("Were you on a break? (yes/no): ")

# Calculate the break time if user was on break
break_time = 0
if on_break.lower() == "yes":
    break_time = float(input("Enter the duration of break in hours: ")) * 3600

try:
    while True:
        # Get the current time
        current_time = time.strftime("%H:%M:%S")

        # Calculate the time difference and money made
        time_diff = get_time_diff(start_time, current_time)
        money_made = calculate_money(time_diff, price_per_hour, break_time)

        # Clear the console output
        os.system("cls" if os.name == "nt" else "clear")

        # Display current time and money made
        print("Current time:", current_time)
        print("Starting time:", start_time)
        print("Price of work: €", price_per_hour)
        print("Money already made: €", format(money_made, ".2f"))

        time.sleep(1)

except KeyboardInterrupt:
    print("\nProgram stopped by the user.")
