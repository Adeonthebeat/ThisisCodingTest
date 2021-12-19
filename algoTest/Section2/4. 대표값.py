
# 대표값
# 10
# 45 73 66 87 92 67 75 79 75 80

n = int(input())
arr = list(map(int, input().split()))
avg = round(sum(arr)/n)
# avg = (sum(arr)/n) + 0.5
# avg = int(avg)
min = 2147000000

for idx, x in enumerate(arr):
    temp = abs(x - avg)
    if temp < min:
        min = temp
        score = x
        res = idx+1
    elif temp == min:
        if x > score:
            score = x
            res = idx + 1


print(avg, res)