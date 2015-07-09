def is_triangle(a,b,c):
    if a<=b+c and b<=a+c and c<=a+b:
        print 'yes'
    else:
        print 'no'
is_triangle(12,3,4)
