'''
Hailey King-Winterton
CSC 500 - Principles of Programming
Critical thinking - M3

24-Hour Clock Alarm:
    Input: current time, wait hours
    Output: alarm time

Pseudocode:
    START
        Prompt user for current time (on a 24-hour clock)
        Store current time

        Prompt user for number of hours they want to wait before alarm goes off
        Store wait hours

        Add current time + number of wait hours to find total number of hours
        Use modulo 24 on total number of hours (wraps result back into 24-hour clock range of 0 through 23)
        Store result as alarm time

        Display message telling user alarm time in 24-hour format
    END
'''
# variables to prompt & store user inputted values
current_time = int(input("Enter the current hour in 24 hour format (0-23): "))
wait_hours = int(input("Enter the number of hours you want to wait: "))

# calculate then wrap in modulo
alarm_time = (current_time + wait_hours) % 24

# output of alarm time in 24-hour format
print(f"The alarm will go off at {alarm_time:02d}:00.")
