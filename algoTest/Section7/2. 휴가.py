# 휴가
# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10
def dfs(idx, sum):
    global ret
    if idx == n + 1:
        if sum > ret:
            ret = sum
    else:
        if idx + t[idx] <= n+1:
            dfs(idx + t[idx], sum + p[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    n = int(input())
    t = list()
    p = list()
    for i in range(n):
        a, b = map(int, input().split())
        t.append(a)
        p.append(b)
    ret = -2147000000
    t.insert(0, 0)
    p.insert(0, 0)
    dfs(1, 0)
    print(ret)
