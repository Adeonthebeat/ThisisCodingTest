# 동전 바꿔주기
# 20
# 3
# 5 3
# 10 2
# 1 5


def dfs(idx, sum):
    global cnt
    if sum > T:
        return

    if idx == k:
        if sum == T:
            cnt += 1
    else:
        for i in range(cn[idx]+1):
            # 중요 sum + (cv[idx] * i)
            dfs(idx + 1, sum + (cv[idx] * i))


if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for _ in range(k):
        p, n = map(int, input().split())
        cv.append(p)
        cn.append(n)
    cnt = 0
    dfs(0, 0)
    print(cnt)

