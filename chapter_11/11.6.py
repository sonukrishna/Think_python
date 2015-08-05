
d={0:0,1:1,2:1,3:2,4:3,5:5}
import time
start_time=time.time()
def fib(n):
   # d={0:0,1:1,2:1,3:2,4:3,5:5}
    if n in d:
	return d[n]
    res=fib(n-1)+fib(n-2)
    d[n]=res
    return res
print fib(10)

#print 'hello'
print("%s seconds",(time.time()-start_time))



start_time2=time.time()
def fib2(n):
   # d={0:0,1:1,2:1,3:2,4:3,5:5}
    if n==0:
	return 0
    elif n==1 or n==2:
	return 1
    else:
	return fib2(n-1)+fib2(n-2)
print fib2(10)
print("%s seconds",(time.time()-start_time2))


    
