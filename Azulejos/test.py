x = [(1, 3, 2), (2, 2, 3), (3, 1, 4), (4, 2, 3)]

print(sorted(x, key=lambda x: (x[1], -x[2])))
