from os import remove

a = set(range(1000))
def f(x):
    A = x in a
    B = x in range(2,21,2)
    C = x in range(5,51,5)
    return (A <= B) and (C <= (not A))

for X in range(1000):
    if not f(X):
        a.remove(X)

print(len(a))


