import datetime 
def p_time(time):
   return time.strftime('%I:%M %p')
time = datetime.datetime.now()
time_format = p_time(time)
print("Time in AM/PM:",time_format)