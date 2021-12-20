
# 8. 곳감(모래시계)
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
# 3
# 2 0 3
# 5 1 2
# 3 1 4

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
s = 0
e = 4
sum = 0

for i in range(m):
    h, t, k = map(int, input().split())

    if t == 0:
        for _ in range(k):
            board[h-1].append(board[h-1].pop(0))
    else:
        for _ in range(k):
            board[h-1].insert(0, board[h-1].pop())


for i in range(n):
    for j in range(s, e+1):
        sum += board[i][j]

    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)