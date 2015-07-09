def fact(n):
    if not isinstance(n,int):
        print 'factorial is only defined for intigers'
        return None
    elif n<0:
        print 'factorial is only defined for positive intigers'
        return None
    elif n==0:
        return 1
    else:
        return n*fact(n-1)
fact(20)
