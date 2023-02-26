from entry_creator import create_entry #creates txt files, input title, date, time, path
from time_convert import convert_24_to_12
from datetime import *
from gather_input import *

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

text_file = ""
n = 1
while current_time + interval_duration <= end_time:
    entry = ""
    entry += "Date:    " + current_time.strftime("%d %B %Y at %I:%M:%S %p") + "\n\n\n"
    entry += "TB" + str(n) + "\n\n\n"
    entry += "TLDR"

    text_file += entry
    current_time += interval_duration + short_break_duration
    if n % long_break_interval == 0:
        current_time += long_break_duration
    n += 1

print(text_file)