def f(s1,s2,m):
    if s1 * s2 >= 600: return not m % 2
    if m == 0: return 0
    h = []
    if s1 >= 3:
        h.append(f(s1-3,s2+3,m-1))
    h.append(f(s1 + 2, s2,m-1))
    return any(h) if m % 2 else all(h)

print([s for s in range(1,15) if (not f(40,s,1)) and f(40,s,2)])
print([s for s in range(1,15) if (not f(40,s,1)) and f(40,s,3)])
print([s for s in range(1,15) if (not f(40,s,2) and f(40,s,4))])
