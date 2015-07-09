def compare():
    print 'x:'
    a=raw_input()
    x=int(a)
    print 'y:'
    b=raw_input()
    y=int(b)
    if x>y:
        print '1'
    elif x==y:
        print '0'
    elif x<y:
        print '-1'
    else:
        print'go fishin'
compare()
