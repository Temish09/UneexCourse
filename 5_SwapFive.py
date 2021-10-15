num = int(input())

answer = num
power = 2
while True and num != 1:
    tmp = answer*num
    answer = tmp*10 + num
    if answer*num == num*10**power + tmp:
        break;
    
    answer %= 10**power
    power += 1

print(answer)