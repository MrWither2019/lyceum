def f(x):
    B = 32 <= x <= 425
    C = 130 <= x <= 480
    D = 290 <= x <= 575
    A = a1 <= x <= a2
    return (C <= (not D)) and A and (not B)

ox = [dx for x in [32,425,130,480,290,575] for dx in (x- 0.01, x , x + 0.01)]
print(ox)
res = []
for a1 in [32,425,130,480,290,575]:
    for a2 in [32,425,130,480,290,575]:
        if a2 > a1 and all(f(x) == 0 for x in ox):
            res.append((a2 - a1))
print(max(res))