# 재귀함수를 이용한 이진수 출력
# 11

def dfs(x):
    if x == 0:
        return
    else:
        dfs(x // 2)
        print(x % 2, end=' ')


if __name__ == "__main__":
    n = int(input())
    dfs(n)
