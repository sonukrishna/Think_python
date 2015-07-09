def gcd(m,n):
    if m<n:
	m,n=n,m
    while True:
        r=m%n
        if r==0:
	    print n
        else:
	    m=n
	    n=r
gcd(4,18)
