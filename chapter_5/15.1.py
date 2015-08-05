'''			lets check fermats theorem			'''


def check_fermats(a,b,c,n):
    lhs=pow(a,n)+pow(b,n)
    rhs=pow(c,n)
    if (n>2) and(lhs==rhs):
	print "holy shit,fermat was wrong"
    else:
	print "it doesnt working"
def user_values():
    prompt="please enter"
    for i in ['a','b','c','n']:
	value=prompt+i+'\n'
    input=raw_input(value)
    float_input=float(input)
    exec('%s=%f' % (i,float_input))
check_fermats(a,b,c,n)
