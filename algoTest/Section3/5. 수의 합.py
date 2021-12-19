
## 외우자.
# 5. 수의 합
# 8 3
# 1 2 1 3 1 1 1 2

n, m = map(int, input().split())
arr = list(map(int, input().split()))

lt = cnt = 0
rt = 1
tot = arr[0]

while True:
    if tot < m:
        if rt < n:
            tot += arr[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= arr[lt]
        lt += 1
    else:
        tot -= arr[lt]
        lt += 1
print(cnt)