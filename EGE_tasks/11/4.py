from math import *
l = 7
power = 26*2
char = ceil(log2(power))
user = ceil(char * l / 8) + 12
print(floor(1024 * 2 / user))
