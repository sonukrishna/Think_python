'''	the function increment as a module	'''

class Time(object):
    def time_to_int(self):
        minute=self.hour*60+self.minute
        second=minute*60+self.second
        return second
#    def int_to_time(second):
#        time=Time()
#        minute,time.second=divmod(second,60)
#        hour,time.minute=divmod(minute,60)
#        time.hour=hour
#        return time
    def increment(self,seconds):
        sec=self.time_to_int()+seconds
	print"the final time:",
        return int_to_time(sec)
    def print_time(self):
        return "hour:minute:seconds=> %.2d:%.2d:%.2d"%(self.hour,self.minute,self.second)
def int_to_time(second):
    time=Time()
    minute,time.second=divmod(second,60)
    hour,time.minute=divmod(minute,60)
    time.hour=hour
    return time

start=Time()
start.hour=9
start.minute=33
start.second=44
print "initial time:",
print start.print_time()
end=start.increment(1568)
print end.print_time()

