from math import *
power = 26*2 + 10
char = ceil(log2(power))
password = ceil(10*char / 8)
print((870 - password * 30) / 30)