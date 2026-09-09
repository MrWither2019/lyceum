#через доп переменную
a = input()
b = input()

temp = a
a = b
b = temp

print("a:",a,"b:", b)

#поменять лениво

c = input()
d = input()

c, d = d, c

print("c:",c,"d:", d)

#поменять олимпиадно

x = int(input())
y = int(input())

x = x + y
y = x - y
x = x - y

print("x:",x,"y:", y)

#поменять сложно

v = int(input())
w = int(input())

v = v ^ w
w = w ^ v
v = v ^ w

print("v:",x,"w:", y)
