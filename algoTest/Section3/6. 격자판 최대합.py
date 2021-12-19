
# 6. 격자판 최대합
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

largest = -2147000000
for i in range(n):
    # sum1 : 행 / sum2 : 열
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += board[i][j]
        sum2 += board[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# sum1 : 왼오대각선 / sum2 : 오왼대각선
sum1 = sum2 = 0
for i in range(n):
    sum1 += board[i][i]
    sum2 += board[i][n-i-1]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

print(largest)

