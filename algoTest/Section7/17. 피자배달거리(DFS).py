# 피자배달거리(DFS)
# 4 4
# 0 1 2 0
# 1 0 2 1
# 0 2 1 2
# 2 0 1 2

def dfs(idx, s):
    global ret
    if idx == m:
        sum = 0
        for j in range(len(hs)):
            x1 = hs[j][0] # 집의 좌표
            y1 = hs[j][1] # 집의 좌표
            dis = 2147000000
            for x in cb: # 피자집
                x2 = pz[x][0]
                y2 = pz[x][1]
                dis = min(dis, abs(x1-x2) + abs(y1-y2))
            sum += dis
        if sum < ret:
            ret = sum
    else:
        for i in range(s, len(pz)):  # 조합
            cb[idx] = i
            dfs(idx + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    hs = []
    pz = []
    cb = [0] * m
    ret = 2147000000
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                hs.append((i, j))
            elif board[i][j] == 2:
                pz.append((i, j))
    dfs(0, 0)
    print(ret)
