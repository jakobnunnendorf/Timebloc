from datetime import *
from gather_input import *

# parse input
start_time = datetime.now().replace(month=int(date_str[3:]), day=int(date_str[:2]), hour=(int(start_time_str[:2])), minute=int(start_time_str[3:]), second=1)
end_time = datetime.now().replace(month=int(date_str[3:]), day=int(date_str[:2]), hour=(int(end_time_str[:2])), minute=int(end_time_str[3:]), second=1)
current_time = start_time
interval_duration = timedelta(minutes=interval_duration)
short_break_duration = timedelta(minutes=short_break_duration)
long_break_duration = timedelta(minutes=long_break_duration)


