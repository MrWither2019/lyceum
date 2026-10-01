def f(x):
    P = 25 <= x <= 64
    Q = 40 <= x <= 115
    A = a1 <= x <= a2
    return P <= ((Q and (not A)) <= (not P))

ox = [dx for x in [25,64,40,115] for dx in (x - 0.01, x, x + 0.01)]

res = []
for a1 in [25,64,40,115]:
    for a2 in [25,64,40,115]:
        if a2 > a1:
            if all(f(x) == 1 for x in ox):
                res.append(a2-a1)
print(min(res))

