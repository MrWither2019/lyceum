def f(s1,s2,m):
    if s1 + s2 >= 171: return not m % 2
    if m == 0: return 0
    h = [f(s1+1,s2,m-1),f(s1,s2+1,m-1),f(s1 * 2,s2,m-1),f(s1,s2*2,m-1)]
    return any(h) if m % 2 else all(h)

# print([s for s in range(1,146) if f(25,s,2)])
print([s for s in range(1,14600) if (not f(25,s,1)) and f(25,s,3)])
print([s for s in range(1,14600) if (not f(25,s,2)) and f(25,s,4)])
