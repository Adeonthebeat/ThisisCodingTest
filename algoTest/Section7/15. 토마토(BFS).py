from collections import deque

# 토마토(BFS)
# 6 4
# 0 0 -1 0 0 0
# 0 0 1 0 -1 0
# 0 0 -1 0 0 0
# 0 0 0 0 -1 1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]

q = deque()
dis = [[0] * n for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            q.append((i, j))

while q:
    temp = q.popleft()
    for i in range(4):
        xx = temp[0] + dx[i]
        yy = temp[1] + dy[i]
        if 0 <= xx < m and 0 <= yy < n and board[xx][yy] == 0:
            board[xx][yy] = 1
            dis[xx][yy] = dis[temp[0]][temp[1]] + 1
            q.append((xx, yy))
flag = 1
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            flag = 0

ret = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > ret:
                ret = dis[i][j]
    print(ret)
else:
    print(-1)

