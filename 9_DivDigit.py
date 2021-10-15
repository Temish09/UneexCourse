def divdigit(num):
    
    digits = [int(n) for n in str(num)]
    
    num_digits = 0
    for n in digits:
        if (n != 0) and (num % n == 0):
            num_digits += 1
    
    return num_digits
