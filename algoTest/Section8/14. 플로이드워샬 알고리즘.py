# 플로이드 워샬 알고리즘
# dis[i][j] = i에서 j로 가는 최소 비용
# dis[i][k] + dis[k][j] =  i에서 k를 거쳐서 j로 가는 최소 비용

# 5 8
# 1 2 6
# 1 3 3
# 3 2 2
# 2 4 1
# 2 5 13
# 3 4 5
# 4 2 3
# 4 5 7


if __name__ == "__main__":
    n, m = map(int, input().split())
    dis = [[5000] * (n + 1) for _ in range(n + 1)]

    # dis[0][0] = 0
    for i in range(1, n + 1):
        dis[i][i] = 0

    for i in range(m):
        a, b, c = map(int, input().split())
        dis[a][b] = c

    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dis[i][j] == 5000:
                print("M", end=' ')
            else:
                print(dis[i][j], end=' ')
        print()
