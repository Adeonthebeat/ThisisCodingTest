import heapq as hq
# 최소힙
# 5
# 3
# 6
# 0
# 5
# 0
# 2
# 4
# 0
# -1

a = []

while True:
    n = int(input())

    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)