
# 자릿수의 합
# 3
# 125 15232 97

n = int(input())
arr = list(map(int, input().split()))

def digit_sum(x):
    sum = 0
    # while x > 0:
    #     sum += x%10
    #     x = x//10
    # return sum
    for xx in str(x):
        sum += int(xx)
    return sum


max = 0
for i in arr:
    tot = digit_sum(i)

    if tot > max:
        max = tot
        res = i

print(res)