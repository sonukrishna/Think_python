'''			class			'''

import math
class Point(object):
    def __init__(self,x,y):
	self.x=x
	self.y=y
    def distance(self,other):
	dx=self.x-other.x
	dy=self.y-other.y
	print math.sqrt(dx**2+dy**2)
first=Point(1,2)
second=Point(3,4)
first.distance(second)

