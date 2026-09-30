def f(s,m):
    if s >= 67 : return not m % 2
    if m == 0: return 0
    h = [f(s + 1, m - 1),f(s + 3, m - 1), f(s * 2, m - 1)]
    return any(h) if m % 2 else all(h)

print([s for s in range(1,67) if (not f(s,1)) and f(s,2)])

33