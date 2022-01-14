from collections import deque
# 0 0 0 0 0 0 0
# 0 1 1 1 1 1 0
# 0 0 0 1 0 0 0
# 1 1 0 1 0 1 1
# 1 1 0 1 0 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 0 0 0

board = [list(map(int, input().split())) for _ in range(7)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dis = [[0] * 7 for _ in range(7)]
Q = deque()
Q.append((0, 0))
board[0][0] = 1

while Q:
    temp = Q.popleft()
    for i in range(4):
        x = temp[0] + dx[i]
        y = temp[1] + dy[i]
        if 0 <= x <= 6 and 0 <= y <= 6 and board[x][y] == 0:
            board[x][y] = 1
            dis[x][y] = dis[temp[0]][temp[1]] + 1
            Q.append((x, y))

if dis[6][6] == 0:
    print(-1)
else:
    print(dis[6][6])



