from collections import deque

# 섬나라 아일랜드(BFS)
# 7
# 1 1 0 0 0 1 0
# 0 1 1 0 1 1 0
# 0 1 0 0 0 0 0
# 0 0 0 1 0 1 1
# 1 1 0 1 1 0 0
# 1 0 0 0 1 0 0
# 1 0 1 0 1 0 0
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 0
            q.append((i, j))
            while q:
                temp = q.popleft()
                for k in range(8):
                    x = temp[0] + dx[k]
                    y = temp[1] + dy[k]
                    if 0 <= x < n and 0 <= y < n and board[x][y] == 1:
                        board[x][y] = 0
                        q.append((x, y))
            cnt += 1
print(cnt)
