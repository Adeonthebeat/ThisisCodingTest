# 수들의 조합
# 5 3
# 2 4 5 8 12
# 6

def dfs(idx, s, sum):
    global cnt
    if idx == k:
        if sum % m == 0:
            cnt += 1
    else:
        for i in range(s, n):
            dfs(idx + 1, i + 1, sum + arr[i])


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    cnt = 0
    dfs(0, 0, 0)
    print(cnt)
