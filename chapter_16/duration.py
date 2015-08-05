'''     this function shows what will the time after a duration of time      '''


class Time(object):
    "time of a day"
start=Time()
start.hour=9
start.minute=45
start.second=0
duration=Time()
duration.hour=1
duration.minute=35
duration.second=0

def add_time(t1,t2):
    sum=Time()
    sum.hour=t1.hour+t2.hour
    sum.minute=t1.minute+t2.minute
    sum.second=t1.second+t2.second
    if sum.second >=60:
	sum.second -=60
	sum.minute +=1
    if sum.minute >=60:
	sum.minute -=60
	sum.hour +=1
    return sum
def print_time(time):
   # p=Time()
    print "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)
total_time=add_time(start,duration)
print_time(total_time)
