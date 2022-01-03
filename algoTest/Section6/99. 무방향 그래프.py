# 무방향 그래프
# 5 5
# 1 2
# 1 3
# 2 4
# 3 4
# 4 5

n, m = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    g[a][b] = 1
    g[b][a] = 1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()