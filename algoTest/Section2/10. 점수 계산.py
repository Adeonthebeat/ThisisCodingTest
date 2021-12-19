
# 10. 점수 계산
# 10
# 1 0 1 1 1 0 0 1 1 0
n = int(input())
arr = list(map(int, input().split()))

sum = 0
cnt = 0

for x in arr:
    if x == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)

