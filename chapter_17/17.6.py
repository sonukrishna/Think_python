class Kangaroo(object):
    def __init__(self,contents=None):
	if contents==None:
	    contents=[]
	self.pouch_contents=contents
    def put_in_pouch(self,item):
	self.pouch_contents.append(item)
    def __str__(self):
	output=[]
	for item in self.pouch_contents:
	    output.append(item)
	return str(output)
kanga=Kangaroo()
roo=Kangaroo()
kanga.put_in_pouch('dear')
kanga.put_in_pouch('fellow')
roo.put_in_pouch('ram')
print kanga
roo.put_in_pouch(kanga)
print roo
print kanga
