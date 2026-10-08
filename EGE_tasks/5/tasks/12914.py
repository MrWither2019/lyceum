res = {}
for i in range(0,2100):
    b = str(bin(i))[2:]
    if i % 3 == 0:
        b = b.replace('0','11')
    else:
        b = b.replace('1','10')
    if (r := int(b, 2)) <= 161: res.update({i : r})

print(res)
print(max(res.items(), key = lambda item: item[1]))
        
