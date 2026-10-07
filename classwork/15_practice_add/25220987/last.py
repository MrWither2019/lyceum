def f(s,m):
    if s <= 12: return not m % 2
    if m == 0: return 0
    h = [f(s - i, m - 1) for i in range(1,6)] + [f(s // 5, m - 1)]
    return any(h) if m % 2 else all(h)

print([s for s in range(20,200) if (not f(s, 1)) and f(s,2)])
print([s for s in range(20,1000) if (not f(s, 1)) and f(s,3)])
print([s for s in range(20,200) if (not f(s, 2)) and f(s,4)])
