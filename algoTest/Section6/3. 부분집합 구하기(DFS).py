# 부분집합 구하기
# 상태트리 잘 구성해보기!

def dfs(v):
    if v == (n + 1):
        for i in range(1, n + 1):
            if ch[i] == 1:
                print(i, end=' ')
        print()
    else:
        ch[v] = 1
        dfs(v + 1)
        ch[v] = 0
        dfs(v + 1)


if __name__ == "__main__":
    n = int(input())
    ch = [0] * (n + 1)
    dfs(1)
