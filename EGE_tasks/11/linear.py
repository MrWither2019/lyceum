from math import log2, ceil, floor
l = 89
power = 26 * 2
char = ceil(log2(power))
one = char * l / 8 + 23
ans = ceil(one * 1536 / 1024)
print(ans)

