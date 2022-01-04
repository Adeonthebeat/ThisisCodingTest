# 휴가
# 3
# 1 5 7
def dfs(idx, sum):
    global ret
    if idx == n:
        if 0 < sum <= s:
            ret.add(sum)
    else:
        dfs(idx + 1, sum + g[idx])
        dfs(idx + 1, sum - g[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    n = int(input())
    g = list(map(int, input().split()))
    s = sum(g)
    ret = set()
    dfs(0, 0)
    print(s - len(ret))

