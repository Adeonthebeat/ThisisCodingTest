# 합이 같은 부분집합
# 6
# 1 3 5 6 7 10
import sys


def dfs(idx, sum):
    if sum > (tot // 2):
        return

    if idx == n:
        if sum == (tot - sum):
            print("YES")
            sys.exit(0)
    else:
        dfs(idx + 1, sum + arr[idx])
        dfs(idx + 1, sum)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tot = sum(arr)
    dfs(0, 0)
    print("NO")
