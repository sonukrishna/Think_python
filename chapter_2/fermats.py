def ferm(a,b,c,n):
    if n>=2:
        if a**n+b**n==c**n:
            print 'Holy smokes,Fermat was wrong!'
        else:
            print 'go fishing,he is right'
ferm(3,4,5,2)
