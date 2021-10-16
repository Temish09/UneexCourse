def squares(w, h, *args):
    screen = [['.'] * w for _ in range(h)]
    for sq in args:
        x, y = sq[0], sq[1]
        size = sq[2]
        ch = sq[3]
        for i in range(size):
            for j in range(size):
                screen[y+i][x+j] = ch
    
    for s in screen:
        for ch in s:
            print(ch, end='')
        print()