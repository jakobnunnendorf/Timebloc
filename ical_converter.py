import pytz
from datetime import datetime
from ics import Calendar, Event

# define the input and output file paths
input_file = 'timeblocks.ics'
output_file = 'timeblocks_SA.ics'

# define the South African time zone
sa_tz = pytz.timezone('Africa/Johannesburg')

# read the input file
with open(input_file) as f:
    cal = Calendar(f.read())

# iterate over each event in the calendar
for event in cal.events:
    # convert the DTSTART time to the South African time zone
    dtstart = event.begin.to(sa_tz).format('YYYYMMDDTHHmmss')

    
    # update the event with the new DTSTART time
    dtend = event.end.to(sa_tz).format('YYYYMMDDTHHmmss')

# write the updated calendar to the output file
with open(output_file, 'w') as f:
    f.write(str(cal))
