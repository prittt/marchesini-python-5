import functools
import time

def time_decorator(funz):
    @functools.wraps(funz)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ret_val = funz(*args, **kwargs)
        end = time.perf_counter()
        print(f"Elapsed {(end-start)*1_000_000:.3f} µs")
        return ret_val
    return wrapper

# @time_decorator
# def Fibonacci(n):
#     cache = [-1] * (n + 1)
#     if n > 1:
#         cache[0] = 1
#         cache[1] = 1
#     def FibonacciRec(n):
#         # if n <= 1:
#         #     return 1

#         if cache[n] == -1:
#             cache[n] = FibonacciRec(n - 1) + FibonacciRec(n - 2)

#         return cache[n]
#     return FibonacciRec(n)

@time_decorator
def FibonacciDict(n):
    cache = {0: 1, 1: 1}
    def FibonacciRec(n):
        # if n <= 1:
        #     return 1

        cache[n] = cache.get(n, FibonacciRec(n - 1) + FibonacciRec(n - 2))
        # if n not in cache:
        #     cache[n] = FibonacciRec(n - 1) + FibonacciRec(n - 2)

        return cache[n]
    return FibonacciRec(n)

def cache_decorator(funz):
    cache = {}
    @functools.wraps(funz)
    def wrapper(*args, **kwargs):
        key = args
        #key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = funz(*args, **kwargs)
        return cache[key]
    return wrapper

@time_decorator
def FibonacciCacheDecorated(n):
    @cache_decorator
    def FibonacciRec(n):
        if n <= 1:
            return 1

        return FibonacciRec(n - 1) + FibonacciRec(n - 2)

    return FibonacciRec(n)

Fibonacci = FibonacciCacheDecorated

print(Fibonacci(1))
print(Fibonacci(2))
print(Fibonacci(3))
print(Fibonacci(4))
print(Fibonacci(5))
print(Fibonacci(6))
print(Fibonacci(7))
