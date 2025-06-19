from print_decorator import print_decorator
#import print_decorator

@print_decorator
def myfun1():
    print('myfun1-a')
    print('myfun1-b')


def myfun2():
    print('myfun2-a')
    print('myfun2-b')


myfun1()
myfun2()
myfun1()
myfun2()