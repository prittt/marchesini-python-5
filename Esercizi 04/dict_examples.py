d = {}
print(type(d))

d[1] = "ciao"
d["2"] = 23.4
d[(1,2)] = [1, 2, 3]

# for v in d.values():
#     # d[k] = "qualcosa"
#     op = d[k] * 2

for k, v in d.items():
    pass

for k in d.keys():
    pass

for k in d:
    pass


print(d.keys())
print(list(d.keys()))

print(d.values())
print(list(d.values()))

print(d.items())
print(list(d.items()))
