def distance(xc,yc,xp,yp):
    import math
    dx=xp-xc
    dy=yp-yc
    diff=dx**2+dy**2
    dist=math.sqrt(diff)
    print dist
def area(dist):
    r=int(dist)
    import math
    a=math.pi*r**2
    print a
def crcl_area(xc,yc,xp,yp):
    r=distance(xc,yc,xp,yp)
    result=area(dist)
    print result
crcl_area(4,5,6,7)    

