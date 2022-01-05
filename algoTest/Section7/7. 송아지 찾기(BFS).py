# 송아지 찾기(BFS)
# 5 14
# 앞으로 1, 뒤로 1, 앞으로 5를 이동
from collections import deque

max_num = 10000
ch = [0] * (max_num + 1)
dis = [0] * (max_num + 1)

n, m = map(int, input().split())
ch[n] = 1
dis[n] = 0
dq = deque()
dq.append(n)

while dq:
    now = dq.popleft() # 5
    if now == m:
        break
    for nxt in (now - 1, now + 1, now + 5):
        if 0 < nxt <= max_num:
            if ch[nxt] == 0: # 4
                dq.append(nxt)
                ch[nxt] = 1
                # 현재 지표 4 채널에 카운트 += 1 ->> dis[4] = 1
                dis[nxt] = dis[now] + 1
print(dis[m])