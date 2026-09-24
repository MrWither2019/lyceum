# a = set()
# def f(x):
#     return (x in range(2,13,2)) <= ((x in range(3,16,3)) and (not (x in a))) <= (not (x in range(2,13,2)))
#
# for X in range(1000):
#     if not f(X):
#         print(X)

a = set(range(1000))
def f(x):
    A = x in a
    P = x in range(2,21,2)
    Q = x in range(5,51,5)
    return (A <= P) and (Q <= (not A))

for x in range(1000):
    if f(x) == 0:
        a.remove(x)
print(len(a))



