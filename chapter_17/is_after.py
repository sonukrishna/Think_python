'''			comparing two times chronologically		'''




class Time(object):
    def time_to_int(self):
        minute=self.hour*60+self.minute
        second=minute*60+self.second
        return second
    def is_after(self,other):
	return self.time_to_int()>other.time_to_int()
start=Time()
start.hour=3
start.minute=44
start.second=56
end=Time()
end.hour=9
end.minute=11
end.second=04
print start.is_after(end)
	
