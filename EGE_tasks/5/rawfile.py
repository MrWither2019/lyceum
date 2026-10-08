'''print(bin(170))
print(oct(170))
print(hex(170))

print(int(0b10101010))
print(int("10101010", 2))'''

def trans(x,n):
    res = ""
    while x > 0:
        c = x % n
        res = str(c) + res
        x = x // n
    return res

print(trans(170,6))
