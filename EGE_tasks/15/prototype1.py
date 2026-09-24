def f(x, a):
    return (a%9 == 0) and ((280 % x == 0) <= ((a%x != 0) <= (730 % x != 0)))
for a in range(1, 1000):
    if all(f(x, a) for x in range(1,100000)):
        print(a)
        break