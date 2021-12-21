from collections import deque

# 8. 침몰하는 타이타닉(그리디)
# 5 140
# 90 50 70 100 60

n, limit = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()

weights = deque(weights)

cnt = 0

while weights:
    if len(weights) == 1:
        break
    if weights[0] + weights[-1] > limit:
        weights.pop()
        cnt += 1
    else:
        #weights.pop(0) # 리스트 앞단 뺴기
        weights.popleft()
        weights.pop()
        cnt += 1
print(cnt)

