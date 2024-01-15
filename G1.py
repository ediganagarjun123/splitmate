import datetime
import os

# Greet the user based on the time of the day
current_time = datetime.datetime.now()
if current_time.hour < 12:
    greeting = "Good morning"
elif current_time.hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"
print(f"{greeting}, {os.getlogin()}. Welcome to your system.")

# Display the full date and time with seconds
print(f"The current date is {current_time.strftime('%A, %B %d, %Y')}.")
print(f"The current time is {current_time.strftime('%I:%M:%S %p')}.")

# Print the operating system and Python version
os.system("hostnamectl | grep 'Operating System:'")
os.system("python --version")
