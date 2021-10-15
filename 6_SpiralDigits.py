M, N = [int(num) for num in input().split(',')]
    
matrix = [([0]*M) for i in range(N)]
path = [([0]*M) for i in range(N)]
direction = 0

def change_dir(direction):
    if direction == 0:
        dx, dy = 1, 0
    elif direction == 1:
        dx, dy = 0, 1
    elif direction == 2:
        dx, dy = -1, 0
    elif direction == 3:
        dx, dy = 0, -1
    return dx, dy

x, y = 0, 0
dx, dy = 1, 0
num = 0
for _ in range(M*N): 
    matrix[y][x] = num
    num += 1
    num %= 10
    
    path[y][x] = 1
        
    if x+dx == M or x+dx < 0:
        direction += 1
    elif y+dy == N or y+dy < 0:
        direction += 1
    elif path[y+dy][x+dx] == 1:
        direction += 1
    direction %= 4
    
    dx, dy = change_dir(direction)
    
    x += dx
    y += dy

for row in matrix:
    print(*row)