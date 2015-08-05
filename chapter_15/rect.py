'''		this find the area of a rectangle		'''

#class Point(object):
class Rect(object):
    def __init__(self,w,h):
	self.width=w
	self.height=h
    def area(self):
	return self.width*self.height
    def perimeter(self) :
	return 2*(self.width+self.height)

rectangle=Rect(50,60)
print rectangle.area()
print rectangle.perimeter()
	    
