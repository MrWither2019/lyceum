def f(a, x, y):
    return ((y + 3*x) < a) or (x > 20) or (y > 40)
for A in range(1,1000):
    if all(f(A, X, Y) for X in range(1,100) for Y in range(1,100)):
        print(A)
