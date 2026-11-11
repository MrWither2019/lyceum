def r (f,s,h):
    if f + s <= 47: return not h % 2
    if h == 0: return 0
    game = [r(f // 3, s,h-1), r(f, s // 3,h-1), r(f - 2, s,h-1), r(f,s - 2,h-1)]
    return any(game) if h % 2 else all(game)

# print([S for S in range(32,100) if r(16,S,2)])
print([S for S in range(32, 1000) if not r(16,S,1) and r(16,S,3)])
print([S for S in range(32, 1000) if r(16,S,4) and (not r(16,S,2))])
