# 4. 마구간 정하기(결정알고리즘)
# 5 3
# 1
# 2
# 8
# 4
# 9

n, c = map(int, input().split())
line = []

for _ in range(n):
    line.append(int(input()))

line.sort()


def countCheck(length):
    cnt = 0
    end_point = line[0]

    for i in range(1, n):
        if line[i] - end_point >= length:
            cnt += 1
    return cnt

lt = 1
rt = line[n - 1]
ret = 0

while lt <= rt:
    mid = (lt + rt) // 2

    if countCheck(mid) >= c:
        ret = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ret)



