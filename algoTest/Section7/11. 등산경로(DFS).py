# 등산경로 문제
# 5
# 2 23 92 78 93
# 59 50 48 90 80
# 30 53 70 75 96
# 94 91 82 89 93
# 97 98 95 96 100

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    if x == ex and y == ey:
        cnt += 1
    else:
        for k in range(4):
            xx = x + dx[k]
            yy = y + dy[k]
            if 0 <= xx < n and 0 <= yy < n and ch[xx][yy] == 0 and board[xx][yy] > board[x][y]:
                ch[xx][yy] = 1
                dfs(xx, yy)
                ch[xx][yy] = 0


if __name__ == "__main__":
    n = int(input())
    board = [[0] * n for _ in range(n)]
    ch = [[0] * n for _ in range(n)]
    max = 0
    min = 0
    sx = sy = ex = ey = 0
    for i in range(n):
        temp = list(map(int, input().split()))

        for j in range(n):
            if temp[j] < min:
                min = temp[j]
                sx = i
                sy = j
            if temp[j] > max:
                max = temp[j]
                ex = i
                ey = j
            board[i][j] = temp[j]
    ch[sx][sy] = 1
    cnt = 0
    dfs(sx, sy)
    print(cnt)
