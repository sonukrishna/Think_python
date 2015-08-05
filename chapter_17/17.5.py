'''	an add method for Points that works with either a Point object or a tuple	'''


class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "%g,%g"% (self.x,self.y)
    def __add__(self,other):
        if isinstance(other,Point):
	    return self.add_point(other)
	if isinstance(other,tuple):
	    return self.add_tup(other)
    def add_point(self,other):
	sumx=self.x+other.x
        sumy=self.y+other.y
        return sumx,sumy
    def add_tup(self,tuple):
	xval=tuple[0]
	yval=tuple[1]
	sumx=self.x+xval
	sumy=self.y+yval
	return sumx,sumy
point1=Point(4,9)
point2=Point(8,3)
print "if added with another point",
print point1+point2
print "if added with a tuple:",
print point1+(5,6,)
