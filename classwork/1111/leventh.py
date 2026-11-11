for i in range(10000,-1,-1):
    n = bin(i)[2:]
    if i % 2 == 0:
        n = '10' + n
    else:
        n = '1' + n + '01'
    res = int(n, 2)
    if res < 30:
        print(i,n,res)


                                                                                        