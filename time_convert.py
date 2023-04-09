def convert_24_to_12(time_24):
    hour, minute = time_24.split(":")
    hour = int(hour)
    if hour == 0:
        hour = 12
        am_pm = "AM"
    elif hour < 12:
        am_pm = "AM"
    elif hour == 12:
        am_pm = "PM"
    else:
        hour -= 12
        am_pm = "PM"
    return f"{hour}:{minute}:00 {am_pm} SGT"