import math

num = int(input())

answer = 'NO'
eps = 1e-10
for base in range(2, int(num**(1/2)) + 1):
    power = math.log(num, base)
    if abs(power - int(power)) < eps:
        answer = 'YES'
        break

print(answer)