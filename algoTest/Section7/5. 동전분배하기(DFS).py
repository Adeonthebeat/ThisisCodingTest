# 동전 분배하기(DFS)
# 7
# 8
# 9
# 11
# 12
# 23
# 15
# 17

def dfs(idx):
    global ret
    if idx == n:
        diff = max(money) - min(money)
        if diff < ret:
            temp = set()
            for i in money:
                temp.add(i)
            if len(temp) == 3:
                ret = diff

    else:
        for i in range(3):
            money[i] += coin[idx]
            dfs(idx + 1)
            money[i] -= coin[idx]


if __name__ == "__main__":
    n = int(input())
    coin = []
    money = [0] * 3
    ret = 2147000000
    for _ in range(n):
        coin.append(int(input()))
    dfs(0)
    print(ret)
