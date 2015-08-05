'''this function takes a number and multiplied with the time and return a new time'''



class Time(object):
    "time of a day"
time=Time()
time.hour=2
time.minute=45
time.second=22

def time_to_int(time):
    minute=time.hour*60+time.minute
    second=minute*60+time.second
    return second
def int_to_time(second):
    box=Time()
    minute,box.second=divmod(second,60)
    box.hour,box.minute=divmod(minute,60)
    return box
def mul_time(time,num):
    bomb=Time()
    sec=time_to_int(time)
    nw_sec=sec*num
    print 'the new time after multiply with %d:' % (num),
    return int_to_time(nw_sec)
def avg_pace(time,distance):
    sec=time_to_int(time)
    vel=sec/distance
    return int_to_time(vel)
#def avg_pace(time):
    #t=Time()
    #t=mul_time(time,n)
 #   print time
def print_time(time):
     return "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)
a=avg_pace(time,9)
new_time=mul_time(time,7)
print print_time(new_time)
print print_time(a)
    
