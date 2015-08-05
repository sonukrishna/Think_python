'''the Point class that takes x and y as optional parameters and assign them corresponding values'''


class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def print_points(self):
	print "the points are: ",
	return "%g,%g"% (self.x,self.y)
points=Point(5.0,7.0)
print points.print_points()
