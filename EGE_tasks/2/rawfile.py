for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x == (not y)) <= (not (w <= x))) or (not z)
                if not f:
                    print(x,y,z,w,'', f)