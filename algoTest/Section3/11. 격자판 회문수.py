
# 11. 격자판 회문수
# 2 4 1 5 3 2 6
# 3 5 1 8 7 1 7
# 8 3 2 7 1 3 8
# 6 1 2 3 2 1 1
# 1 3 1 3 5 3 2
# 1 1 2 5 6 5 2
# 1 2 2 2 2 1 5

cnt = 0
board = [list(map(int, input().split())) for _ in range(7)]

boardHalf = 7//2

for i in range(boardHalf):
    for j in range(7):
        temp = board[j][i:i+5]

        # 행 회문 체크
        if temp == temp[::-1]:
            cnt += 1

        # 열 회문 체크 ->> 5개만 회문 비교 ->> 5//2 = 2
        for k in range(2):
            if board[i+k][j] != board[i+5-k-1][j]:
                break
        else:
            cnt += 1
print(cnt)

