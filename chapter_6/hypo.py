def hypotenuse():
    import math
    print 'one side'
    a=raw_input()
    x=int(a)
    print 'other side'
    b=raw_input()
    y=int(b)
    sqr=x**2+y**2
    hypo=math.sqrt(sqr)
    print 'the hypertenuse is',hypo
hypotenuse()
