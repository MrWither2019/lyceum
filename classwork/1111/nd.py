for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((x or y) <= z) or (y == w) or z
                if not F:
                    print(w,x,y,z,'',F)
    