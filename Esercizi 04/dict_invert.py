def dict_invert_v01(d):
    inverted = {}
    for k in d:
        inverted[d[k]] = k
    return inverted

def dict_invert_v02(d):
    inverted = {}
    for k, v in d.items():
        inverted[v] = k
    return inverted

def dict_invert_v03(d):
    inverted =  {v: k for k, v in d.items()}
    return inverted


if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5, 6]
    d = {e: e*2 for e in lista}
    d = {}
    for e in lista:
        d[e] = e * 2

    students = {
        'Theodore': 10,
        'Mathew': 11,
        'Roxanne': 9,
    }
    students_inverted = dict_invert_v01(students)
    print(students)
    print(students_inverted)

    students_inverted = dict_invert_v02(students)
    print(students)
    print(students_inverted)

    students_inverted = dict_invert_v03(students)
    print(students)
    print(students_inverted)