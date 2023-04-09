# create_event takes summary_str (title of the event), end time (YYYYMMDDTHHMMSS) and start time (YYYYMMDDTHHMMSS)
from event import create_event

# import user input
from gather_input import *

# generate schedule
schedule = "" # empty string to collect all events
n = 1
while current_time + interval_duration <= end_time:
    schedule += create_event(f"TB{n}", current_time.strftime("%Y%m%dT%H%M%S"), (current_time + interval_duration).strftime("%Y%m%dT%H%M%S"))
    current_time += interval_duration + short_break_duration
    if n % long_break_interval == 0:
        current_time += long_break_duration
    n += 1