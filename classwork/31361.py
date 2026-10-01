def d(a,b):
    return not a % b
def f(a,x):
    return d(x, 33) <= ((not d(x, a)) <= (not d(x,242)))
for A in range(1000,1,-1):
    if all([f(A,X) for X in range(1000)]):
        print(A)
        break