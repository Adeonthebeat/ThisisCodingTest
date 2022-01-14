from collections import deque

# 5 2
# 60 50 70 80 90
# 6 0
# 60 60 90 60 60 60

n, m = map(int, input().split())
q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

dq = deque(q)
cnt = 0
while True:
    current = dq.popleft()

    if any(current[1] < x[1] for x in dq):
        dq.append(current)
    else:
        cnt += 1
        if current[0] == m:
            print(cnt)
            break
