import os
import datetime
from ics import Calendar
from ics import Event
import pytz  # pip install pytz

# Get input from user
date_str = input("Enter target date (DD-MM): ")
start_time_str = input("Enter workday start time (HH:MM 24h): ")
end_time_str = input("Enter workday end time (HH:MM 24h): ")

# Check if user wants to use standard template
use_template = input("Standard template? (y/n) ").lower() == "y"
if use_template:
    interval_duration = 25
    short_break_duration = 5
    long_break_interval = 4
    long_break_duration = 15
else:
    interval_duration = int(input("Enter interval duration in minutes: "))
    short_break_duration = int(input("Enter short break duration in minutes: "))
    long_break_interval = int(input("Enter number of intervals before long break: "))
    long_break_duration = int(input("Enter long break duration in minutes: "))

# Parse input
target_date = datetime.datetime.now().replace(month=int(date_str[3:]), day=int(date_str[:2]))
start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
interval_duration = datetime.timedelta(minutes=interval_duration)
short_break_duration = datetime.timedelta(minutes=short_break_duration)
long_break_duration = datetime.timedelta(minutes=long_break_duration)

# Get current timezone
current_country = input("Are you in Singapore? (y/n) ").lower() == "y"
if current_country:
    current_tz = pytz.timezone('Asia/Singapore')  # replace with your desired time zone identifier
else:
    current_country = input("where are you? (country code f.e. DE, SG, ZA)").lower()
    current_tz = pytz.timezone(pytz.country_timezones(current_country)[0])  # convert string to timezone object

# Generate time blocks
time_blocks = []
current_time = datetime.datetime.combine(target_date, start_time)
while datetime.datetime.combine(target_date, current_time.time()) + interval_duration <= datetime.datetime.combine(target_date, end_time):
    time_blocks.append(current_time)
    current_time += interval_duration + short_break_duration
    if len(time_blocks) % long_break_interval == 0:
        current_time += long_break_duration

# Create calendar events
c = Calendar()
for i, tb in enumerate(time_blocks):
    event = Event()
    event.name = f"TB{i+1}"
    event.begin = current_tz.localize(tb)  # set time zone
    event.duration = interval_duration
    c.events.add(event)

# Write to file
filename = "timeblocks.ics"
with open(filename, "w") as f:
    f.write(str(c))

# Open in calendar app
os.system(f"open {filename}")

# You can run this program in a terminal by navigating to the directory where the program is saved and running:
# python timeblocks.py
