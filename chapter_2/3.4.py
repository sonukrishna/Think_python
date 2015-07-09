def do_twice(n,arg):
    n(arg)
    n(arg)
def print_twice(arg):
    print arg
    print arg
do_twice(print_twice,'spam')
def do_four(n,arg):
    do_twice(n,arg)
    do_twice(n,arg)
do_four(print_twice,'spam')
