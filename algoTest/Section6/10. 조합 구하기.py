# 조합 구하기
# 4 2

def dfs(idx, s):
    global cnt
    if idx == m:
        for j in range(idx):
            print(ret[j], end=' ')
        cnt += 1
        print()
    else:
        for i in range(s, n + 1):
            ret[idx] = i
            dfs(idx + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    ret = [0] * (n + 1)
    cnt = 0
    # 조합 1부터 시작
    dfs(0, 1)
    print(cnt)
