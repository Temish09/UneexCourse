def BinPow(a, N, f):
    if N == 1:
        return a
    if N % 2 == 0:
        result = BinPow(a, N // 2, f)
        result = f(result, result)
    else:
        result = f(a, BinPow(a, N-1, f))
    
    return result
