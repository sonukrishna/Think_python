def do_twice(n):
    n()
    n()
def do_four(n):
    do_twice(n)
    do_twice(n)
def leng():
    print "+--------",
def wdth():
    print"|        ",
def do_leng():
    do_four(leng)
    print"+"
def do_wdth():
    do_four(wdth)
    print"|"
def raw():
    do_leng()
    do_four(do_wdth)
def grid():
    do_four(raw)
    do_leng()
grid()



