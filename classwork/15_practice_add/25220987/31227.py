def f(s1,s2,m):
    if s1 + s2 <= 53: return not m % 2
    if m == 0: return 0
    h = [f(s1-3,s2,m-1),f(s1,s2-3,m-1),f(s1//3,s2,m-1),f(s1,s2//3,m-1)]
    return any(h) if m % 2 else all(h)

# print([s for s in range(35,150) if f(19,s,2)])
# print([s for s in range(35,10000) if (not f(19,s,1)) and f(19,s,3)])
print([s for s in range(35,200) if (not f(19,s,2)) and f(19,s,4)])