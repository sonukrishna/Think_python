'''	    add method for the Point class.		'''


class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "%g,%g"% (self.x,self.y)
    def __add__(self,other):
	sumx=self.x+other.x
	sumy=self.y+other.y
	print "the new point after sum is :",
	return sumx,sumy
print 'first set points:',
point1=Point(10.5,6.25)
point2=Point(8.33,9.56)
print point1
print "second set of points :",
print point2
print point1+point2
