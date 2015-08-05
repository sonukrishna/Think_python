'''		boolean function for the chronological order		  '''


class Time(object):
    "represents the time of a day"
#time=Time()
time1=Time()
time1.hour=12
time1.minute=59
time1.second=30
time2=Time()
time2.hour=11
time2.minute=59
time2.second=30
def compute(time):
    return time.hour+(time.minute/60)+(time.second/3600)
def is_after(time1,time2):
    hour1,minute1,second1=time1.hour,time1.minute,time1.second
    hour2,minute2,second2=time2.hour,time2.minute,time2.second
    print "the chronological order says that,it is:",
    return compute(time1)<compute(time2)
print is_after(time1,time2)
