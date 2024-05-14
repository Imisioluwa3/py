# Get the process ID (PID) of an error

# log = "July 31 07:51:48 my computer bad_process[12345]: ERROR Performing package upgrade"
# index = log.index("[")
# print(log[index+1:index+6])

# Thoughh this will bring up issues if the PID is short than 5 character and there are more than one []

import re

log = "July 31 07:51:48 my computer bad_process[1345]: ERROR Performing package upgrade"
regex = r"\[(\d+)]"
result = re.search(regex, log)
print(result[1])