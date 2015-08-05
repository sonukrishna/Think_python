

import math
def sqrt(n):
   # print 'the estimate value:',
    b=0.75*float(n)
    eps=0.000001
   # if n==0:
    #    return 0
   # if n==1:
    #    return 1
    while True:
      #  print b
        x=(b+(n/b))/2
        if abs(x-b)<eps:
	    return b
	else:
            b=x
        
for n in range(1,10):
    print n, "\t",
    print sqrt(n),"\t",
    print math.sqrt(n),"\t",
    print abs(sqrt(n)-math.sqrt(n))

