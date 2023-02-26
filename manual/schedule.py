# create_event takes summary_str (title of the event), end time (YYYYMMDDTHHMMSS) and start time (YYYYMMDDTHHMMSS)
from event import create_event
import datetime

# import user input
from gather_input import *

# parse input
target_date = datetime.datetime.now().replace(month=int(date_str[3:]), day=int(date_str[:2]))
start_time = target_date.replace(hour=int(start_time_str[:2]), minute=int(start_time_str[3:]), second=1)
end_time = target_date.replace(hour=int(end_time_str[:2]), minute=int(end_time_str[3:]), second=1)
interval_duration = datetime.timedelta(minutes=interval_duration)
short_break_duration = datetime.timedelta(minutes=short_break_duration)
long_break_duration = datetime.timedelta(minutes=long_break_duration)

# generate schedule
schedule = "" # empty string to collect all events
current_time = start_time
n = 1
while current_time + interval_duration <= end_time:
    schedule += create_event(f"TB{n}", current_time.strftime("%Y%m%dT%H%M%S"), (current_time + interval_duration).strftime("%Y%m%dT%H%M%S"))
    current_time += interval_duration + short_break_duration
    if n % long_break_interval == 0:
        current_time += long_break_duration
    n += 1