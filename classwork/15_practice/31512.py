def d(a,b):
    return not a % b
B = [i for i in range(70,91)]
def f(A):
    return all([d(x, A) or ((x in B) <= (not d(x, 22))) for x in range(1,1000)])
for i in range(10000, 1, -1):
    if(f(i)):
        print(i)
        break