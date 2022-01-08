# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
            dfs(xx, yy)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    ret = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt = 0
                dfs(i, j)
                ret.append(cnt)
    print(len(ret))
    ret.sort()

    for x in ret:
        print(x)