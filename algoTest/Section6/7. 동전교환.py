
# 동전 교환
# 3
# 1 2 5
# 15

# 5
# 1 5 7 11 15
# 39


def dfs(idx, sum):
    global ret

    if idx > ret:
        return

    if sum > m:
        return

    if sum == m:
        if idx < ret: # idx 동전의 사용 개수.
            ret = idx
    else:
        for i in range(n):
            dfs(idx + 1, sum + arr[i])



if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    ret = 2147000000
    arr.sort(reverse=True)
    dfs(0, 0)
    print(ret)