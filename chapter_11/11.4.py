'''REVERSE LOOKUP'''

def reverse_lookup(d,v):
    a=[]
    for i in d:
	if i not in a:
	    if d[i]==v:
		a.append(i)
    for j in a:
	print j 

d={'a':2,'b':2,'c':2,'d':2}
reverse_lookup(d,2)
