'''			increment		'''


class Time(object):
    "time of a day"
time=Time()
time.hour=2
time.minute=45
time.second=0

def time_to_int(time):
    minute=time.hour*60+time.minute
    second=minute*60+time.second
    return second
def int_to_time(second):
    time=Time()
    minute,time.second=divmod(second,60)
    hour,time.minute=divmod(minute,60)
    time.hour=hour
    return time
def increment(time,seconds):
    sec=time_to_int(time)
    new_sec=sec+seconds
    return int_to_time(new_sec)
def print_time(time):
     return "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)
new_time=increment(time,6365)
print print_time(new_time)
