from entry_creator import create_entry #creates txt files, input title, date, time, path
from time_convert import convert_24_to_12
from months import months
from datetime import *

# Gather dates and times
year = datetime.now().year # Get the current year

input_date = input("Enter the date (DD-MM): ") # let user input date
day = input_date.split("-")[0]
month = months[int(input_date.split("-")[1])-1]
date = day + " " + month + " " + str(year) # date in correct format

standard_template = input("Do you want to use the standard template? (y/n): ") # let user input standard template
if standard_template == "y":
    start_time = convert_24_to_12("06:00")
    end_time = convert_24_to_12("22:00")
    block_duration = 25
    number_of_blocks = 4
    short_break_duration = 5
    long_break_duration = 15
else:
    input_start_time = input("Enter time in 24 hour format (HH:MM): ") # let user input start time
    start_time = convert_24_to_12(input_start_time)

    input_end_time = input("Enter time in 24 hour format (HH:MM): ") # let user input end time
    end_time = convert_24_to_12(input_end_time)

    input_block_duration = input("Enter block duration (in minutes): ") # let user input block duration
    block_duration = int(input_block_duration)

    input_number_of_blocks = input("Enter number of blocks: ") # let user input number of blocks
    number_of_blocks = int(input_number_of_blocks)

    input_short_break_duration = input("Enter short break duration (in minutes): ") # let user input short break duration
    short_break_duration = int(input_short_break_duration)

    input_long_break_duration = input("Enter long break duration (in minutes): ") # let user input long break duration
    long_break_duration = int(input_long_break_duration)

#create_entry("TB1", date, start_time, "/Users/jakobnunnendorf/Github/DayOne-templates/test")

# create_entry("TB2", "28 January 2023", "1:48:56 PM SGT", "/Users/jakobnunnendorf/Github/DayOne-templates/test")

# Create the files
start_time_obj = start_time.replace(" SGT", "") # remove the " SGT" from the time
start_time_obj = datetime.strptime(date + " " + start_time_obj, '%d %B %Y %I:%M:%S %p') # convert to datetime object
# prints: 2023-01-01 06:00:00
end_time_obj = end_time.replace(" SGT", "") # remove the " SGT" from the time
end_time_obj = datetime.strptime(date + " " + end_time_obj, '%d %B %Y %I:%M:%S %p') # convert to datetime object
#prints: 2023-01-01 22:00:00
print(end_time_obj)
current_time_obj = start_time_obj # set current time to start time

def add_short_break(input_time, short_break_duration):
    input_time = input_time + timedelta(minutes=short_break_duration)
    return input_time

def add_long_break(input_time, long_break_duration):
    input_time = input_time + timedelta(minutes=long_break_duration)
    return input_time

def add_block_duration(input_time, block_duration):
    input_time = input_time + timedelta(minutes=block_duration)
    return input_time

# first_line = "    Date:    " + entry_date + " at " + entry_time + "\n"
#     second_line = "    Location:	" + "\n" + "\n"
#     body = entry_title + "\n\nTLDR:\n\nResults:\n\nComments:\n\n"
#     entry_template = first_line + second_line + body
entry_path = "/Users/jakobnunnendorf/Github/DayOne-templates/test"

tb_counter = 1

entry_content = ""

while current_time_obj <= end_time_obj:
    for i in range(number_of_blocks):
        if current_time_obj <= end_time_obj:
            # add content
            entry_title = "TB" + str(tb_counter)
            entry_date = date
            entry_time = current_time_obj.strftime("%I:%M:%S %p SGT")

            first_line = "Date:    " + entry_date + " at " + entry_time + "\n"
            content = entry_title + "\n" + "TLDR:\n\nResults:\n\nComments:\n\n"
            entry_template = first_line + "\n" + "\n" + content + "\n" + "\n"

            entry_content += entry_template

            print("added entry: " + entry_title + " on " + entry_date + " at " + entry_time)
            tb_counter += 1
            # add block duration to current time
            current_time_obj = add_block_duration(current_time_obj, block_duration)
            # add short break
            current_time_obj = add_short_break(current_time_obj, short_break_duration)
    # add long break
    current_time_obj = add_long_break(current_time_obj, long_break_duration)

create_entry("TBs", entry_content, entry_path)