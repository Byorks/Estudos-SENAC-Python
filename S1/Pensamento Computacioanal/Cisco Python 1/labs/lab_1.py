# 2.6.11   LAB   Operators and expressions – 2
# Scenario
# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.

# For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16.

# Test your code carefully. Hint: using the % operator may be the key to success.

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Dividing per hour
end_hour = int(dura / 60)

end_mins = dura % 60

mins += end_mins

# Now I need to verify if mins + end_mins surpass 1 hour
end_hour += mins // 60 # is the same thing end_hour += int (mins / 60)

mins %= 60

print("end_hour:", end_hour)
# Sum to the currently hour
hour += end_hour

# How can I now if surpass 24 hours?
hour %= 24

print(hour, mins, sep=":")
