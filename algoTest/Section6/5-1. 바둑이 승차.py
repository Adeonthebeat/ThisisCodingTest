# 바둑이 승차(DFS)
# 259 5
# 81
# 58
# 42
# 33
# 61

def dfs(idx, sum, tsum):
    global ret
    # 해당 레벨과 해당 레벨 밑의 값이 현재 결과보다 작다면, return.
    if sum + (tot - tsum) < ret:
        return

    if sum > c:
        return

    if idx == e:
        if sum >= ret:
            ret = sum
    else:
        dfs(idx + 1, sum + arr[idx], tsum + arr[idx])
        dfs(idx + 1, sum, tsum + arr[idx])


if __name__ == "__main__":
    c, e = map(int, input().split())
    arr = []
    for i in range(e):
        arr.append(int(input()))
    tot = sum(arr)
    ret = 0

    dfs(0, 0, 0)
    print(ret)
