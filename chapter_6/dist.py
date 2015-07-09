def distnc():
    import math
    print 'first point,x1'
    a=raw_input()
    x1=int(a)
    print 'second point,x2'
    b=raw_input()
    x2=int(b)
    print 'first point,y1'
    c=raw_input()
    y1=int(c)
    print 'second point,y2'
    d=raw_input()
    y2=int(d)
    dx=x2-x1
    dy=y2-y1
    dsqr=dx**2+dy**2
    res=math.sqrt(dsqr)
    print 'the distance b/w the lines is:',res
distnc()
