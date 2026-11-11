a = 5**2004 - 5**1016 - 25**508 - 5**400 + 25**250 - 27
res = 0
while a > 0:
    c = a % 5
    if c == 4:
        res += 1
    a = a // 5
print(res)