from ics_calendar import *
from TB_WB_generator import *

with open("timeblocks.ics", "w") as f:
    f.write(template)

with open("dayone.txt", "w") as f:
    f.write(text_file)