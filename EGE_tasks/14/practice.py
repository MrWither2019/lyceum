# for x in range(29):
#     a = 4*29**7 + 6*29**6 +3 *29**5 +x *29**4 +7*29**3 +9*29**2 + 2*29 + 1
#     b = 8*29**7 + 2*29**6 +4*29**5 +1*29**4 +x*29**3 +1*29**2 + 5*29 + 3
#     if (a + b) % 28 == 0: print(x, (a+b) // 28)

# for x in range(2400,-1,-1):
#     a =  7*9**210 + 6*9**110 - x
#     counter = 0
#     while a:
#         if (a % 9) == 0: counter += 1
#         a = a // 9
#     if counter == 100:
#         print(x)
#         break

# a = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
# res = 0
# while a:
#     if a % 27 > 9: res += 1
#     a = a//27
# print(res)

# for x in '0123456789abcdefghi':#jklmnoprs #tuvwxyz
#     a = int(f'2e{x}g8',19)
#     b = int(f'6f{x}bg',19)
#     if (a + b) % 18 == 0:
#         print(int(x,19), (a+b) // 9)

res = [-1,0]
for x in range(1,9431):
    a = 39**483 + 39**235 - x
    counter = 0
    while a:
        if a % 39 == 0:
            counter += 1
        a = a // 39
    if counter > res[1]:
        res = [x, counter]
print(res)

# for x in range(1, 500000):
# for p in range(36, 11 ,-1):
#     res = [(int('29a1', p) + int('47771', p) + int('12a',p) \
#             == 1000000 + x) for x in range(1,500000)]
#     if any(res):
#         print(p)

# for p in range(7,100):
#     a = 2*p**6 + 4*p**5 +6*p**4 +5*p**3 +1*p**2 +2*p+3
#     b = 2*p**5 + 5*p**4 +1*p**3 +3*p**2 +4*p**1 +1*p**0
#     if (a + b) % 17 == 0:
#         print(p, (a+b) // 17)

# res = 0
# a = 30 * 36**231 + 18*6**101 - 3*36**45 - 2357
# while a:
#     c = a % 36
#     st = c % 5 == 0
#     nd = c % 3 == 0
#     if st ^ nd:
#         res += 1
#     a = a // 36
# print(res)

# a = 3**72 + 6*3*50 - 7*3**36 + 2*3**15 + 155
# a9 = ''
# while a:
#     a9 += str(a % 9)
#     a = a // 9
# print(len(set(a9)))

# a =11*15**65 + 18*15**38 - 14*15**17 + 19*15**11 +18338
# a15 = ''
# while a:
#     a15 += str(a % 15)
#     a = a // 9
# print(len(set(a15)))

# from copy import copy
# a = 39*15**64 + 35**450 + 74*43**121 - 450035
# res = [-1,0]
# for p in range(9,100):
#     ac = copy(a)
#     an = ''
#     while ac:
#         an += str(ac)
#         ac = ac // p
#     ts = an.count('8')
#     if res[1] < ts:
#         res = [p, ts]
# print(res)

# res = 0
# for x in range(1,1000):
#     a = 7**500 + 7**200 - 7**50 - x
#     counter = 0
#     while a:
#         counter += a % 7
#         a = a // 7
#     res = max(res,counter)
# print(res)
    

# for x in range(0,100000):
#     a = 4**2015 + 2**x -  2**2015 + 15
#     if bin(a).count('1') == 500:
#         print(x)
#         break


# for x in range(0,100000):
    # counter = 0
    # a = 36**17 - 6**x + 71
    # while a:
    #     counter += a % 6
    #     a = a // 6
    # if counter == 61:
    #     print(x)
    #     break

# a = 5*216**1156 - 4*36**1147 +6**1153 - 875
# pyat = 0
# nuli = 0
# while a:
#     c = a % 6
#     if c == 5:
#         pyat += 1
#     if c == 0:
#         nuli += 1
#     a = a // 6
# print(pyat - nuli)

# a = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 -4*3**2024 - 2029
# res = 0
# while a:
#     if a % 27 > 9 :
#         res += 1
#     a = a // 27
# print(res)

# for x in range(1,3000):
#     counter = 0
#     a = 9**150 + 9**30 - x
#     while a:
#         if a % 9 == 0:
#             counter += 1
#         a = a // 9
#     if counter == 122:
#         print(x)
#         break

