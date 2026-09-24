from math import *
power = 4100
l = 101
char = ceil(log2(power))
id = ceil(char * l / 8)
print(ceil(id * 2048 / 1024))
