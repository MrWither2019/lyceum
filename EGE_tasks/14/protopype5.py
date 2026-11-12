for x in range(3000,0,-1):
    a = 9*11**210 + 8 * 11**150 - x 
    counter = 0
    while a:
        c = a % 11
        if c == 0:
            counter += 1
        a = a // 11
    if counter == 60:
        print(x)
        break