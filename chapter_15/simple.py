'''		distance		'''

import math
class Point(object):
    "an object in 2d space"
blank=Point()
blank.x=3.0
blank.y=4.0
def print_point(p):
    dist=math.sqrt(p.x**2+p.y**2)
    print dist
print_point(blank)
