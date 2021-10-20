import decimal
from decimal import Decimal

A = Decimal(input())
E = int(input())

decimal.getcontext().prec = E

def tan1(x, n=1000):
    result = Decimal(2*n+1)
    for i in range(n, 0, -1):
        result = Decimal(2*i-1) - Decimal(x)**2 / Decimal(result)
    
    return Decimal(x) / Decimal(result)

def get_pi(n=2500):
    res = Decimal(0)
    for k in range(0, n):
        res += Decimal(-1)**k / (Decimal(3)**k * Decimal(2*k + 1))
    return 2*Decimal(3).sqrt() * res


pi = get_pi()
angle = A / 200 * pi

res = str(tan1(angle))
print(res)
size = len(res.split('.')[1])

decimal.getcontext().prec = 1000
pi = get_pi()
angle = A / 200 * pi

res = str(round(tan1(angle), size))

print(res)