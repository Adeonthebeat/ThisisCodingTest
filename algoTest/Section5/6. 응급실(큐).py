from collections import deque
# 6. 응급실(큐)
# 5 2
# 60 50 70 80 90

n, m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]

Q = deque(Q)
cnt = 0

while True:
    cur = Q.popleft()
    # 위급한 사람 체크.
    if any(cur[1] < x[1] for x in Q):
        Q.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
