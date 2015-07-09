''' FUNCTION BISECT REDUCE THE TIME COMPLEXITY OF SEARCHING'''


def bisect(lst,obj):
    beg=0
    end=len(lst)-1
    while(beg<=end):
	mid=(beg+end)/2
	if lst[mid]==obj:
	    return mid
	    break
	elif obj>lst[mid]:
	    beg=mid+1
	else:
	    end=mid-1
    if beg<=end:
	print 'The indx of the obj:',
	return mid+1
    else:
	return 'nothing found!'

lst1=list('asdfghjklpoiuytrewqzxcvbnm')
lst1.sort()
print lst1
print bisect(lst1,'w')
