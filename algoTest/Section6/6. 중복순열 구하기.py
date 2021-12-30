import sys


# input = sys.stdin.readline()
# 3 2
# 6 2

def dfs(v):
    global cnt
    if v == m:
        for j in range(m):
            print(ret[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            ret[v] = i
            dfs(v + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    cnt = 0
    ret = [0] * m
    dfs(0)
    print(cnt)