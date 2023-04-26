# create_event takes summary_str (title of the event), end time (YYYYMMDDTHHMMSS) and start time (YYYYMMDDTHHMMSS)
from event import create_event

# import user input
from gather_input import *

# generate schedule
schedule = ""  # empty string to collect all events
n = 1
while current_time + interval_duration <= end_time:
    # Create the study interval event
    schedule += create_event(f"TB{n}", current_time.strftime("%Y%m%dT%H%M%S"), (current_time + interval_duration).strftime("%Y%m%dT%H%M%S"))
    current_time += interval_duration
    
    # Check if it's time for a long break
    if n % long_break_interval == 0:
        # Create the long break event
        schedule += create_event(f"{long_break_duration.seconds // 60}min Break", current_time.strftime("%Y%m%dT%H%M%S"), (current_time + long_break_duration).strftime("%Y%m%dT%H%M%S"))
        current_time += long_break_duration
    else:
        # Create the short break event
        schedule += create_event(f"{short_break_duration.seconds // 60}min Break", current_time.strftime("%Y%m%dT%H%M%S"), (current_time + short_break_duration).strftime("%Y%m%dT%H%M%S"))
        current_time += short_break_duration
    n += 1
