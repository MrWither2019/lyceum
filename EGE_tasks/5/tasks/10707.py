def trans(x,base):
    r = ''
    while x > 0:
        r = str(x % base) + r
        x = x // base
    return r

res = {}
for i in range(1,300):
    s = trans(i,6)
    if i % 3 == 0:
        s = s + s[:2]
    else:
        s = s + trans((i % 3) * 10, 6)
    if (r := int(s, 6)) > 680:
        res.update({i:r})

print(sorted(res.items(), key = lambda item: item[1]))
    
