def bisection(array, target_value):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target_value:
            return mid
        if array[mid] < target_value:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def reversemy(m):
    for i in range(len(m) // 2):
        m[i], m[-i - 1] = m[-i - 1], m[i]

def Ceasar(m):
    st = m[0]
    for i in range(len(m) - 1):
        m[i] = m[i + 1]
    m[-1] = st

def evklidNOD(st, nd):  #recieve 2 ints by default
    while nd:
        st, nd = nd, st % nd
    return st

def coutSquare(sideLen, symbol):    #simple solid console square
    for i in range(sideLen):
        print(symbol * sideLen)

def reverseInt(var):    #return reversed int
    var = str(var)
    return int(var[::-1])

from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(10000)
@lru_cache(maxsize=None)
def fibonacci(index): #return number and time
    if index <= 0:
        return 0
    elif index == 1:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)