from collections import deque

# 사과나무(BFS)
# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
sum = 0
ch = [[0] * n for _ in range(n)]
q = deque()

# 시작점 중간
ch[n // 2][n // 2] = 1
sum += arr[n // 2][n // 2]
q.append((n // 2, n // 2))

level = 0
while True:
    if level == (n // 2):
        break
    size = len(q)
    for i in range(size):
        temp = q.popleft()
        for j in range(4):
            x = temp[0] + dx[j]
            y = temp[1] + dy[j]
            if ch[x][y] == 0:
                sum += arr[x][y]
                ch[x][y] = 1
                q.append((x, y))
    level += 1

print(sum)

