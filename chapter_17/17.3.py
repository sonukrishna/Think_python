


class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
	print "the points are:",
	return "%g,%g"% (self.x,self.y)
points=Point(10.05,6.25)
print points
