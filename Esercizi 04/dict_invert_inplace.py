from dict_invert import dict_invert_v03 as div03

#import dict_invert as di

def dict_invert_inplace(d):
    inverted = dict_invert_v03(d)
    d.clear()
    d.update(inverted)

students = {
    'Theodore': 10,
    'Mathew': 11,
    'Roxanne': 9,
}
dict_invert_inplace(students)
print(students)