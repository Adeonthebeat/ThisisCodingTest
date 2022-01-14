
# 5
# 172 67
# 183 65
# 180 70
# 170 72
# 181 60

n = int(input())
man = []
for _ in range(n):
    h, w = map(int, input().split())
    man.append((h, w))

# 키 순으로 정렬! 개발자의 킥!!
man.sort(reverse=True)

cnt = largest = 0

for h, w in man:
    if w > largest:
        largest = w
        cnt += 1
print(cnt)