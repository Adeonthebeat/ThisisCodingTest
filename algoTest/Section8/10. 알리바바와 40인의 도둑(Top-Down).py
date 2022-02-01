# 메모이제이션
# dfs(n, n) - 최소비용으로 올 수 있도록 재귀호출(min)

# 5
# 3 7 2 1 9
# 5 8 3 9 2
# 5 3 1 2 3
# 5 4 3 2 1
# 1 7 5 2 4

def dfs(x, y):
    if dy[x][y] > 0:
        return dy[x][y]

    if x == 0 and y == 0:
        return arr[0][0]
    else:
        # 열
        if y == 0:
            dy[x][y] = dfs(x - 1, y) + arr[x][y]
        elif x == 0:
            dy[x][y] = dfs(x, y - 1) + arr[x][y]
        else:
            dy[x][y] = min(dfs(x - 1, y), dfs(x, y - 1)) + arr[x][y]

        return dy[x][y]


if __name__ == "__main__":
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)]
    print(dfs(n - 1, n - 1))
