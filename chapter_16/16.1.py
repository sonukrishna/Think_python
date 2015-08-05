'''			time			'''


class Time():
	'''represents the time of the day'''
time=Time()
time.hour=11
time.minute=3
time.second=30

def print_time(time):
   # p=Time()
    print "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)
print_time(time)
