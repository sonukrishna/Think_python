def sqrt(n):
    print 'the estimate value:',
    a=raw_input()
    b=float(a)
    if n==0:
	return 0
    if n==1:
        return 1
    while True:
	print b
	x=(b+(n/b))/2
	if x==b:
	    print 'the root is:',x
	    break
	b=x
print sqrt(8)
