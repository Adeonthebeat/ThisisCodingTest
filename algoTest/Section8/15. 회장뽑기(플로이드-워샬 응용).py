## 플로이드 워셜은 삼중 포문으로 완성
# 5
# 1 2
# 2 3
# 3 4
# 4 5
# 2 4
# 5 3
# -1 -1


if __name__ == "__main__":
    # 최단거리가 회장 후보
    # 첫째 줄은 회장 후보의 점수와 회장후보 수를 출력
    # 두 번째 줄은 회장 후보를 모두 출력
    n = int(input())
    dis = [[100] * (n + 1) for _ in range(n + 1)]

    # 같은 값은 0으로 세팅.
    for i in range(1, n + 1):
        dis[i][i] = 0

    # 값 받기
    while True:
        a, b = map(int, input().split())
        if a == -1 and b == -1:
            break
        dis[a][b] = 1
        dis[b][a] = 1

    # 플로이드 워셜
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])

    # for x in dis:
    #     print(x)

    res = [0] * (n + 1)
    score = 100
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res[i] = max(res[i], dis[i][j])
        score = min(score, res[i])

    out = []
    for i in range(1, n + 1):
        if res[i] == score:
            out.append(i)

    print('%d %d' % (score, len(out)))
    for i in out:
        print(i, end=' ')
