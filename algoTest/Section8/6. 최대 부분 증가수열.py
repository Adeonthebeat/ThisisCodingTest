# 8
# 5 3 7 8 6 2 9 4

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0) # 뒤로 밀기 위해
dy = [0] * (n + 1)
dy[1] = 1
ret = 0

for i in range(2, n + 1):
    max = 0
    for j in range(i - 1, 0 , -1):
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1

    if dy[i] > ret:
        ret = dy[i]
print(ret)