import functools
import builtins

# def print_decorator(funz):
#     def wrapper(*args, **kwargs):
#         print("--- Marchesini ---", end="")
#         return funz(*args, **kwargs)

#     return wrapper    

# @print_decorator
# def myfun1():
#     print('myfun1-a')
#     print('myfun1-b')


# myfun1()


def print_decorator(funz):
    @functools.wraps(funz)
    def wrapper(*args, **kwargs):
        #global print
        old_print = builtins.print
        def myprint(*args, **kwargs):
            old_print("--- Marchesini ---", end="")
            old_print(*args, **kwargs)
        builtins.print = myprint
        funz(*args, **kwargs)
        builtins.print = old_print
    return wrapper

