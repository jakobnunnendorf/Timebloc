import datetime

test = True

if test:
    date_str = "01-01"
    start_time_str = "08:00"
    end_time_str = "17:00"
    use_template = True
else:
    date_str = input("Enter target date (DD-MM): ")
    start_time_str = input("Enter workday start time (HH:MM 24h): ")
    end_time_str = input("Enter workday end time (HH:MM 24h): ")
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

# parse input
target_date = datetime.datetime.now().replace(month=int(date_str[3:]), day=int(date_str[:2]))
start_time = target_date.replace(hour=int(start_time_str[:2]), minute=int(start_time_str[3:]), second=1)
end_time = target_date.replace(hour=int(end_time_str[:2]), minute=int(end_time_str[3:]), second=1)
interval_duration = datetime.timedelta(minutes=interval_duration)
short_break_duration = datetime.timedelta(minutes=short_break_duration)
long_break_duration = datetime.timedelta(minutes=long_break_duration)

current_time = start_time