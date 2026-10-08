def alg(n):
    nbin = bin(n)[2:]
    if n % 2 == 0:
        nbin += '01'
    else:
        nbin = '1' + nbin + '1'
    return(int(nbin , 2))
    


for i in range(1,300):
    if (n:= alg(i)) > 156:
        print(i, n)
        break
        
