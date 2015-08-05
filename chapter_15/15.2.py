'''	   move a rectangle by adding dx,dy to the corner		'''


class Point(object):
    'its a point in space'
class Rectangle(object):
    'a rectangle with width and height'
rect=Rectangle()
left=Point()
left.x=3.0
left.y=4.0
right=Point()
right.x=10.0
right.y=4.0
rect.corner1=left
rect.corner2=right
dx=3.0
dy=3.0
	
def move_rectangle(rect,dx,dy):
    print ('corner1 is: (%g,%g)' %(rect.corner1.x,rect.corner1.y))
    print ('corner2 is: (%g,%g)' %(rect.corner2.x,rect.corner2.y))
    print ('the rectangle moved dx %g,dy %g'% (dx,dy))
    rect.corner1.x += dx
    rect.corner1.y += dy
    rect.corner2.x += dx
    rect.corner2.y += dy
    print ('corner1 changed by (%g,%g):' %(rect.corner1.x,rect.corner1.y))
    print ('corner2 changed by (%g,%g):' %(rect.corner2.x,rect.corner2.y))
move_rectangle(rect,dx,dy)
