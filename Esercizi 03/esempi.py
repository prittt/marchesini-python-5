import time
import functools

def time_decorator(funz):
    @functools.wraps(funz)
    def wrapper(*args, **kwargs):
        start = time.time()
        ret_val = funz(*args, **kwargs)
        end = time.time()
        print(f"Elapsed {end-start}s")
        return ret_val
    return wrapper


@time_decorator
def mcd(a,b):
    import math
    return math.gcd(a,b)


@time_decorator
def remove_dup_v1(inlist: list):
    return list(set(inlist))

@time_decorator
def remove_dup_v2(inlist: list):
    outlist = []
    for e in inlist:
        if e not in outlist:
            outlist += [e]  # outlist.append(e)
    return outlist

print(remove_dup_v1.__name__)

# def time(funz, inlist):
#     start = time.time()
#     ret_val = funz(inlist)
#     end = time.time()
#     print(f"Elapsed {end-start}s")
#     return ret_val


inlist = list(range(1, 1000000, 3))

ret = remove_dup_v1(inlist)
ret = mcd(23, 45)
ret = remove_dup_v2(inlist)

#remove_dup_v1 = time_decorator(remove_dup_v1)
#remove_dup_v2 = time_decorator(remove_dup_v2)


# remove_dup_v1_decorated(inlist)
# remove_dup_v2_decorated(inlist)

# start = time.time()
# remove_dup_v1(inlist)
# end = time.time()
# print(f"Elapsed {end-start}s")

# start = time.time()
# remove_dup_v2(inlist)
# end = time.time()
# print(f"Elapsed {end-start}s")
