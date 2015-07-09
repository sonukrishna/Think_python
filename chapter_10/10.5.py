'''THE FUNCTION TAKES THE LIST AND RETURN TRUE IF THERE IS ANY ELEMENT APPEAR MORE THAN ONCE'''

def has_duplicates(lst):
    for i in lst:
	if lst.count(i)>1:
	    return True
	else:
	    return False

lst1=[1,2,3,4,5,6,7,8,9]
print has_duplicates(lst1)
lst2=list('abrakadabra!')
print has_duplicates(lst2)
