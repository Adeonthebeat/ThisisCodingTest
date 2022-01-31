# 밑면의 넓이는 고정(내림차순)
# 무게가 기준으로 비교하면서 높이를 세팅.
# 무게가 무거우면 꼭대기 놓지 못함
# dy[4] ->> 제일 꼭대기 있을 때, 최대 높이
# 5
# 25 3 4
# 4 4 6
# 9 2 3
# 16 2 5
# 1 5 2

if __name__ == "__main__":

    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True) # 밑면의 넓이는 고정(내림차순)

    dy = [0] * n
    dy[0] = bricks[0][1]
    ret = bricks[0][1]

    for i in range(1, n):
        max_height = 0
        # bricks[i][2] = 만들고자 하는 벽돌
        for j in range(i - 1, -1, -1):
            # 무게 비교 및 높이 비교
            if bricks[j][2] > bricks[i][2] and dy[j] > max_height:
                max_height = dy[j]
        dy[i] = max_height + bricks[i][1]
        ret = max(ret, dy[i])
    print(ret)



