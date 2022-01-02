import sys


# 수열 추측하기
# 4 16

def dfs(idx, sum):
    if idx == n and sum == m:
        for x in ret:
            print(x, end=' ')
        sys.exit()
    else:
        for j in range(1, n + 1):
            if ch[j] == 0:
                ch[j] = 1
                ret[idx] = j
                dfs(idx + 1, sum + (ret[idx] * b[idx]))
                ch[j] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    ret = [0] * n
    b = [1] * n
    ch = [0] * (n + 1)

    # 가장 중요한 부분
    for i in range(1, n):
        b[i] = b[i - 1] * (n - i) // i

    dfs(0, 0)
