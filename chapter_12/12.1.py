'''	THIS FUNCTION TAKE ANY NO.OF ARGUMENTS AND RETURNS THEIR SUM	'''


def sumall(*arg):
    sum=0
    for i in arg:
	sum=sum+i
    print 'The sum is:',
    return sum

print sumall(55,66,44,2,8,63,22,58)
