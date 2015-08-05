'''		the increment function without modifying the passing object		'''



class Time(object):
    "time of a day"
time=Time()
time.hour=9
time.minute=45
time.second=0

def increment (t,seconds):
    box=Time()
    t.second += seconds
    box.second=t.second
    box.minute=t.minute
    box.hour=t.hour
    if box.second>=60:
        mint,sec=divmod(box.second,60)
        box.second=sec
        box.minute += mint
    if box.minute >=60:
        hr,mint=divmod(box.minute,60)
        box.minute=mint
        box.hour += hr
    return box
def print_time(time):
   # p=Time()
    print "hour:minute:seconds=> %.2d:%.2d:%.2d"%(time.hour,time.minute,time.second)

total_change=increment(time,3450)
print_time(total_change)

