
# 8. 뒤집은 소수
# 5
# 32 55 62 3700 250

n = int(input())
arr = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True




for x in arr:
    temp = reverse(x)

    if isPrime(temp):
        print(temp, end= ' ')