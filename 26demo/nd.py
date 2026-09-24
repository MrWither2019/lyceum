for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                res = ((x == (not y)) <= (not (w <= x))) or (not z)
                if res == 0 : print(w,x,y,z, '', res)
                