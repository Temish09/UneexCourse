x, y, r = [int(item) for item in input().split(',')]

answer = 'YES'

while True:
    dot_x, dot_y = [int(item) for item in input().split(',')]
    if (dot_x == 0) and (dot_y == 0):
        break
    if (dot_x-x)**2 + (dot_y-y)**2 > r*r:
        answer = 'NO'

print(answer)