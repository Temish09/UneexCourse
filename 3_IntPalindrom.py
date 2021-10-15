num = int(input())
num_clone = num
num_revers = 0

while num_clone != 0:
    num_revers = num_revers*10 + num_clone % 10
    num_clone //= 10
    
answer = 'YES' if num_revers == num else 'NO'
print(answer)