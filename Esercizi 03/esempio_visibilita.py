# #include <stdio.h>
# int x = 5;

# void change_global() {
#     int x;

#     printf("%i", x);
#     x = 10;
# }

# x = 5
# def change_global():
#     global x
#     print(x)
#     x = 10

# change_global()
# print(x)

reg_print = print
def myprint(*args, **kwargs):
    reg_print('Marchesini: ', end='')
    reg_print(*args, **kwargs)

def myfun1():
    print('myfun1-a', 5, sep='*')
    print('myfun1-b')

print = myprint
myfun1()
print = reg_print

print("Fine")
