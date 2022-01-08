# 단지번호붙이기(BFS)
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
cnt = 0
ret = []
q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            q.append((i, j))
            cnt = 1
            while q:
                temp = q.popleft()
                for k in range(4):
                    xx = temp[0] + dx[k]
                    yy = temp[1] + dy[k]
                    if xx < 0 or xx >= n or yy < 0 or yy >= n or board[xx][yy] == 0:
                        continue
                    board[xx][yy] = 0
                    q.append((xx, yy))
                    cnt += 1
            ret.append(cnt)

print(len(ret))
ret.sort()
for i in ret:
    print(i)