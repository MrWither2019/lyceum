def f(a,x,y):
    return (x + y <= 27) or (y <= x - 1) or (y >= a)
for A in range(1000,1,-1):
    if all(f(A,X,Y) for X in range(1000) for Y in range(1000)):
        print(A)
        break