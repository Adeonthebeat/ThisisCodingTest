# 공주 구하기
# 8 3
## 7
from collections import deque
n, k = map(int, input().split())
dq = list(range(1, n+1))

dq = deque(dq)

while dq:
    cnt = 0
    for _ in range(k-1):
        x = dq.popleft()
        dq.append(x)
    dq.popleft()

    if len(dq) == 1:
        print(dq[0])
        dq.popleft()

