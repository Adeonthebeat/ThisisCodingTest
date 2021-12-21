
# 6. 씨름 선수(그리디)
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

n = int(input())
body = []

for _ in range(n):
    k, m = map(int, input().split())
    body.append((k, m))

body.sort(reverse = True)

cnt = 0
largest = 0

for k, m in body:
    if m > largest:
        largest = m
        cnt += 1

print(cnt)



