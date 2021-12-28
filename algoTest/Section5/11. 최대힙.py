import heapq as hq
# 최대힙
# 최소힙의 반대. -부호를 붙여서 입력 후, -부호를 붙여서 출력
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
            print(-hq.heappop(a))
    else:
        hq.heappush(a, -n)