'''	__cmp__ method for time objects 	'''



class Time(object):
    def __init__(self,hour,minute,second):
	self.hour=hour
	self.minute=minute
	self.second=second
    def time_to_int(self):
	minute=self.hour*60+self.minute
	second=minute*60+self.second
	return second
    def __cmp__(self,other):
	time1=self.time_to_int()
	time2=other.time_to_int()
	return cmp(time1,time2)
time1=Time(3,55,34)
time2=Time(4,00,01)
print time1.__cmp__(time2)
