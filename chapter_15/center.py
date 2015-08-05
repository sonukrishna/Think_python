'''		center of a rectangle		'''


class Point(object):
    "a point in 2d space"
class Rectangle(object):
    "a rectangle with width,height,corners"

rect=Rectangle()
rect.width=100.0
rect.height=200.0
rect.corner=Point()
rect.corner.x=3.0
rect.corner.y=4.0

def find_center(rect):
    box=Point()
    box.x=rect.corner.x+rect.width/2.0
    box.y=rect.corner.y+rect.height/2.0
    print "the center is:",
    return box
def print_point(p):
    print "(%g,%g)"%(p.x,p.y)

center=find_center(rect)
print_point(center)
