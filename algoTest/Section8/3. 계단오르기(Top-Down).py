
def dfs(cnt):

    # Cut Edge
    if dy[cnt] > 0:
        return dy[cnt]

    if cnt == 1 or cnt == 2:
        return cnt
    else:
        dy[cnt] = dfs(cnt - 1) + dfs(cnt - 2)
        return dy[cnt]


if __name__ == "__main__":
    n = int(input())
    dy = [0] * (n + 1)
    print(dfs(n))
