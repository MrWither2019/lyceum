res = {}
for N in range(1,500):
    R = bin(N)[2:]
    R = R.replace('1', '!')
    R = R.replace('0', '1')
    R = R.replace('!', '0')
    R = '1' + R
    if R.count('1'):
        R += '1'
    else: R += '0'
    if (r := int(R,2)) > 180:
        res.update({N: (R, r)})

print(*sorted(res.items(), key = lambda item: item[0])[:10], sep = '\n')
    
    
    
