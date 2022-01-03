# 최대점수 구하기
# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4

def dfs(idx, sum, time):
    global ret
    if time > m:
        return

    if idx == n:  # 문제의 개수
        if sum > ret:
            ret = sum

    else:
        dfs(idx + 1, sum + pv[idx], time + pt[idx])
        dfs(idx + 1, sum, time)


if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    ret = -2147000000
    for _ in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)

    dfs(0, 0, 0)

    print(ret)