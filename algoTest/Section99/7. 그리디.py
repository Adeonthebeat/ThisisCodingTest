
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50
n = int(input())
box = list(map(int, input().split()))
m = int(input())
box.sort()

for _ in range(m):
    box[0] += 1
    box[n-1] -= 1
    box.sort()

print(box[n-1] - box[0])