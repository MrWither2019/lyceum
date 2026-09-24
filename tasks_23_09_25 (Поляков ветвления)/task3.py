a = {}
keys = ['A','B','C']
values = map(int, input().split())
add = zip(keys,values)
a.update(dict(add))
a = sorted(a.items(), reverse = True)
print(a[0])
#[0] == a[1] == a[2]:
 #   print(a[0].key, a[1].key, a[2].key)
#elif a[0] == a[1]:
 #  print(a[0].key, a[1].key)
#else:
 # print(a[0].key)
