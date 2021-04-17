def Up_Down_Left_Right(N):
    N = int(N)

    # 변수명 잊지마~!
    row, col = 1, 1
    # directions = input().split()
    directions = ['R', 'R', 'R', 'U', 'D', 'D']

    x_row = [0, 0, -1, 1]
    x_col = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for dir in directions:
        for i in range(len(move_types)):
            if dir == move_types[i]:
                d_row = row + x_row[i]
                d_col = col + x_col[i]
        if d_row < 1 or d_col < 1 or d_row > N or d_col > N:
            continue
        row, col = d_row, d_col

    return row, col


def time_cnt(N):
    cnt = 0
    for i in range(N + 1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    cnt += 1

    return cnt


def Chess(data):
    # The_Royal_Night

    # ord 주의!
    row = int(data[1])
    col = int(ord(data[0]) - ord('a')) + 1

    # count
    cnt = 0

    # steps
    steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

    for step in steps:
        x_row = row + step[0]  # step[0] 주의!
        y_col = col + step[1]  # step[1] 주의!

        if 1 <= x_row <= 8 and 1 <= y_col <= 8:
            cnt += 1

    return cnt






if __name__ == "__main__":

    # print(Up_Down_Left_Right(5))
    # print(time_cnt(5))
    # print(Chess('a1'))

    ### Development of Game ###
    n, m = 4, 4

    # Map Initialization
    d = [[0] * m for _ in range(n)]

    # x, y, direction
    x, y, direction = 1, 1, 0
    d[x][y] = 1

    array = []
    for i in range(n):
        array.append(list(map(int, input().split())))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]


    # 왼쪽으로 회전
    def turn_left():
        global direction
        direction -= 1
        if direction == -1:
            direction = 3

    # Simulation
    count = 1
    turn_time = 0
    while True:
        # 왼쪽으로 회전
        turn_left()
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 가보지 않은 곳이 존재한다면
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
        else:
            turn_time += 1

        # 4개의 방향을 다 돌았다면
        if turn_time == 4:
            nx = x - dx[direction]
            ny = y - dy[direction]

            if array[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0

    # print(count)