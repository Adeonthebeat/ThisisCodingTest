# 순열 구하기
# 3 2

def dfs(idx):
    global cnt
    if idx == m:
        for j in range(idx):
            print(ret[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n + 1):
            if ch[i] == 0:
                ch[i] = 1
                ret[idx] = i
                dfs(idx + 1)
                ch[i] = 0


if __name__ == "__main__":
    n, m = map(int, input().split())
    ch = [0] * (n + 1)
    ret = [0] * n
    cnt = 0
    dfs(0)
    print(cnt)
