def f(x):
    B = 290 <= x <= 750
    C = 135 <= x <= 675
    A = a1 <= x <= a2
    return ((not B) and C) <= (((not A) and C) <= B)

ox = [dx for x in [290, 750, 135, 675] for dx in (x - 0.01, x, x + 0.01)]

res = []
for a1 in [290, 750, 135, 675]:
    for a2 in [290, 750, 135, 675]:
        if a2 > a1:
            if all(f(x) == 1 for x in ox):
                res.append(a2-a1)
print(min(res))

