def check_fermat():
    print 'first number'
    a=raw_input()
    e=int(a)
    print 'second no'
    b=raw_input()
    f=int(b)
    print 'third no:'
    c=raw_input()
    g=int(c)
    print 'the power is:'
    n=raw_input()
    m=int(n)
    if n>=2:
        if e**m+f**m==g**m:
            print 'Holy smokes,Fermat was Wrong!'
        else:
            print 'that doesnt work'

check_fermat()

