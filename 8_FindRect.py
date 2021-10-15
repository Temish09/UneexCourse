m = [input()]
a = input()
m.append(a)
while a[0] != '-':
    a = input()
    m.append(a)
    

M = len(m)
N = len(m[0])

count = 0
for i in range(M-1):
    for j in range(N-1):
        a0 = m[i][j]
        a1 = m[i][j+1]
        a2 = m[i+1][j]
        a3 = m[i+1][j+1]
        if (a0 != '#') and (a1 != '#') and (a2 != '#') and (a3 == '#'):
            count += 1

print(count)
