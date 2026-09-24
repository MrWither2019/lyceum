def getNum(number, i):
    i = i-1
    number = abs(number)
    return (number % 10 ** (4 - i)) // 10 ** (4 - i-1)

a = int(input())
print(
    (getNum(a,1) + getNum(a,2))*
    (getNum(a,2) + getNum(a,3))*
    (getNum(a,3) + getNum(a,4))
    )


     
    
    
