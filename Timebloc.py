import os
import datetime
from ics import Calendar, Event #pip install ics

# Get input from user
date_str = input("Enter target date (DD-MM): ")
start_time_str = input("Enter workday start time (HH:MM 24h): ")
end_time_str = input("Enter workday end time (HH:MM 24h): ")
interval_duration = int(input("Enter interval duration in minutes: "))
short_break_duration = int(input("Enter short break duration in minutes: "))
long_break_interval = int(input("Enter number of intervals before long break: "))
long_break_duration = int(input("Enter long break duration in minutes: "))

# Parse input
target_date = datetime.datetime.strptime(date_str, "%d-%m").date()
start_time = datetime.datetime.strptime(start_time_str, "%H:%M").time()
end_time = datetime.datetime.strptime(end_time_str, "%H:%M").time()
interval_duration = datetime.timedelta(minutes=interval_duration)
short_break_duration = datetime.timedelta(minutes=short_break_duration)
long_break_duration = datetime.timedelta(minutes=long_break_duration)

# Generate time blocks
time_blocks = []
current_time = datetime.datetime.combine(target_date, start_time)
while current_time.time() < end_time:
    time_blocks.append(current_time)
    current_time += interval_duration + short_break_duration
    if len(time_blocks) % long_break_interval == 0:
        current_time += long_break_duration

# Create calendar events
c = Calendar()
for i, tb in enumerate(time_blocks):
    event = Event()
    event.name = f"TB{i+1}"
    event.begin = tb
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
