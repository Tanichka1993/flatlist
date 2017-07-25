a_list = [1, 2, 3, [1, 2], 2, [1, [1, 3]], 20]

i = 0
while i < (len(a_list)):
    while isinstance(a_list[i], list):
        a_list[i: i + 1] = a_list[i]
    i += 1
print(a_list)
