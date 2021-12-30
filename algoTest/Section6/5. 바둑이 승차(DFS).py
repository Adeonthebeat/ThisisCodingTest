# 바둑이 승차(DFS)
# 259 5
# 81
# 58
# 42
# 33
# 61

def dfs(idx, sum):
    global ret

    if sum > c:
        return
    if idx == e:
        if sum >= ret:
            ret = sum
    else:
        dfs(idx + 1, sum + arr[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    c, e = map(int, input().split())
    arr = []
    ret = 0
    for i in range(e):
        arr.append(int(input()))
    tot = sum(arr)
    dfs(0, 0)
    print(ret)
