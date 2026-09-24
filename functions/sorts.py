from random import randint
def bubble(M):  #sort current
    for i in range(len(M) - 1):
        for j in range(len(M) - 2, i-1, -1):
            if M[j + 1] < M[j]:
                M[j+1], M[j] = M[j], M[j + 1]

def selection(m):   #sort current
    n = len(m)
    for i in range(n):
        min_index = i
        for j in range(i, n):
            if m[min_index] > m[j]:
                min_index = j
        m[i], m[min_index] = m[min_index], m[i]

def quick(m):       #return sorted
    n = len(m)
    if n <= 1:
        return m
    else:
        pivot = m[n // 2]
        lesser = [i for i in m if i < pivot]
        middle = [i for i in m if i == pivot]

        greater = [i for i in m if i > pivot]
        return quick(lesser) + middle + quick(greater)

def merge(a, b):
    na = len(a)
    nb = len(b)
    ia = 0
    ib = 0
    res = []
    while ia < na and ib < nb:
        if a[ia] < b[ib]:
            res.append(a[ia])
            ia += 1
        else:
            res.append(b[ib])
            ib += 1
    return res + a[ia:] + b[ib:]

def merge_sort(a):
    if len(a) == 1: return a
    mid = len(a) // 2
    l = merge_sort(a[:mid])
    r = merge_sort(a[mid:])
    return merge(l, r)

import numpy as np
def quicker(m):
    n = m.size
    if n <= 1:
        return m
    pivot = np.median((m[0], m[n // 2], m[-1]))
    lesser = m[m < pivot]
    equal = m[m == pivot]
    greater = m[m > pivot]
    return np.concatenate((quicker(lesser), equal, quicker(greater)))

def InsSort(m):
    n = len(m)
    if n <= 1:
        return
    for i in range(1, n):
        key = m[i]
        j = i - 1
        while j >= 0 and key < m[j]:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key

def quickIns(m):       #return sorted
    n = len(m)
    if n <= 1:
        return m
    if n <= 32:
        return InsSort(m)
    else:
        pivot = m[n // 2]
        lesser = [i for i in m if i < pivot]
        middle = [i for i in m if i == pivot]
        greater = [i for i in m if i > pivot]
        return quick(lesser) + middle + quick(greater)


