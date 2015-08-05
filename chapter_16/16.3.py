'''		increment function without loops		'''


class Time(object):
    "time of a day"
time=Time()
time.hour=9
time.minute=45
time.second=0

def increment (time,seconds):
    time.second += seconds
    if time.second>=60:
	mint,sec=divmod(time.second,60)
	time.second=sec
	time.minute += mint
    if time.minute >=60:
	hr,mint=divmod(time.minute,60)
	time.minute=mint
	time.hour += hr
    return time
def print_time(time):
   # p=Time()
    print "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)

total_change=increment(time,1450)
print_time(total_change)
