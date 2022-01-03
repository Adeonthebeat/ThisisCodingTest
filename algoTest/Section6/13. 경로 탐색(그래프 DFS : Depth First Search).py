# 13. 경로 탐색(그래프 DFS : Depth First Search)
# 5 9
# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 5
# 3 4
# 4 2
# 4 5

def dfs(idx):
    global cnt
    if idx == n:
        cnt += 1
        for x in path:
            print(x, end=' ')
        print()
    else:
        for i in range(1, n + 1):
            if g[idx][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                dfs(i)
                path.pop()
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    ch = [0] * (n + 1)
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
    cnt = 0
    path = [1]
    ch[1] = 1  # 1번 노드 체크
    dfs(1)
    print(cnt)
    print(cnt)

