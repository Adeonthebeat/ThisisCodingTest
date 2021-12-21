
# 7. 창고 정리(그리디)
# 10
# 69 42 68 76 40 87 14 65 76 81
# 50

n = int(input())
storage = list(map(int, input().split()))
m = int(input())
storage.sort()

for _ in range(m):
    storage[0] += 1
    storage[n-1] -= 1
    storage.sort()

print(storage[n-1] - storage[0])