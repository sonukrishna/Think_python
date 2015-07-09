''' THE FUNCTION TAKES A LIST AND RETURNS A NEW LIST WITH ONLY UNIQUE ELEMENTS FROM THE ORIGINAL'''


def remove_duplicates(lst):
    res=[]
    for i in lst:
	if i not in res:
	    res.append(i)
    return res

lst1=[1,2,3,1,2,3,12,14,2,22,2,223]
print remove_duplicates(lst1)
lst2=list('abrakadabra!')
print remove_duplicates(lst2)



''' SINCE IT CONSUMES O(N**2) TIME COMPLEXITY,WE CAN SOLVE IT USING SET '''

def remove_d(lst):
    s=list(set(lst))
    return s
lst3=[1,2,12,1,2,1,2,12,12]
print remove_d(lst3)
