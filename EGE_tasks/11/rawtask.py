from math import *

i = ceil(log2(10 + 62))
N = 5895222
V = 23 * 1024**2
one = V // N * 8

print(one // i + 1)