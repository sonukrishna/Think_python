'''	THE FUNCTION INVERTS THE DICTIONARY	'''




def invert_dict(d):
    inv={}
    for key in d:
	value=d[key]
	if value not in inv:
	    inv[value]=[key]
	else:
	    inv[value].append(key)
    return inv


d={'m':1,'g':3,'o':1,'n':1,'i':2,'d':3,'s':2}
print invert_dict(d)
