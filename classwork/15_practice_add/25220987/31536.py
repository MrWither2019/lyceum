def f(s1,s2,m):
    if s1 + s2 >= 133 : return not m % 2
    if m == 0: return 0
    h = [f(s1 + 4, s2, m - 1),f(s1 * 2, s2, m - 1),f(s1, s2 + 4, m - 1),f(s1, s2 * 2, m - 1)]
    return any(h) if m % 2 else all(h)

# print([s for s in range(1,116) if f(17,s,2)])
# print([s for s in range(1,116) if (not f(17,s,1) and f(17,s,3))])
print([s for s in range(1,116) if (not f(17,s,2) and f(17,s,4))])

