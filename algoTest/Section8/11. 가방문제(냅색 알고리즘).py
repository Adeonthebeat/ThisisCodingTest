# 냅색 알고리즘 : Knapsack algorithm
# dy[j] : 가방에 j라는 무게까지 담을 때, 보석의 최대 가치
# 좋으면 바꿔주고, 아니면 홀드

# 4 11
# 5 12
# 3 8
# 6 14
# 4 8


if __name__ == "__main__":
    # 보석 종류의 개수와 가방에 담을 수 있는 무게의 한계값
    n, m = map(int, input().split())
    dy = [0] * (m + 1)

    for i in range(n):
        w, v = map(int, input().split())

        for j in range(w, m + 1):
            dy[j] = max(dy[j], dy[j - w] + v)

    print(dy[m])
