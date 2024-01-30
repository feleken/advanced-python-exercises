def hailstone_func(n):
    hailstone_nums = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
            hailstone_nums.append(n)
        else:
            n = 3 * n + 1
            hailstone_nums.append(n)
    return hailstone_nums

hailstone_dict = dict()
for i in range(1, 50):
    new_data = {i: len(hailstone_func(i))}
    hailstone_dict.update(new_data)

print(hailstone_dict)