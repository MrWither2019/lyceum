from itertools import product
letters = [['А', 'К', 'Ц', 'Е', 'Н', 'Т']] * 6
perms = list(enumerate(list(product(*letters))))
for i in range(100):
    print(perms[i])
    # if i[0] % 2 == 0 and i[1][0] != 'А' and i[1][0] != 'Е' and i[1][0] != 'К' and 'Т' in i[1]:
    #         print(i[0])
    #         break 
