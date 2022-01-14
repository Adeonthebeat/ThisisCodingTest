from collections import deque
# 5 140
# 90 50 70 100 60

n, limit = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()

cnt = 0

weights = deque(weights)
while weights:
    if len(weights) == 1:
        break
    if weights[0] + weights[-1] > limit:
        weights.pop()
        cnt += 1
    else:
        weights.popleft()
        weights.pop()
        cnt += 1

print(cnt)
