# 밑면의 넓이는 고정(내림차순)
# 무게가 기준으로 비교하면서 높이를 세팅.
# 무게가 무거우면 꼭대기 놓지 못함
# dy[4] ->> 제일 꼭대기 있을 때, 최대 높이


if __name__ == "__main__":
    n = int(input())
    bricks = []

    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True) # 밑면의 넓이는 고정(내림차순)
    dy = [0] * n
    # 높이 (bricks[0][0] = 밑변 넓이 / bricks[0][2] = 무게)
    dy[0] = bricks[0][1]
    ret = bricks[0][1]
    for i in range(1, n):
        max_height = 0
        # bricks[i][2] = 만들고자 하는 벽돌
        for j in range(i - 1, 0, -1):
            if bricks[j][2] > bricks[i][2] and dy[j] > max_height:
                max_height = dy[j]
            dy[i] = max()
