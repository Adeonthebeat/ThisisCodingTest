# 중복을 막기위해 1차원 배열로 거꾸로 해결
# 2차원 배열은 복잡도가 높아짐.

# 5 20
# 10 5
# 25 12
# 15 8
# 6 3
# 7 4


if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m + 1)

    for i in range(n):
        ps, pt = map(int, input().split())

        for j in range(m, pt-1, -1):
            dy[j] = max(dy[j], dy[j-pt] + ps)

    print(dy[m])