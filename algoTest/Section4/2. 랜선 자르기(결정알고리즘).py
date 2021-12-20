
# 2. 랜선 자르기(결정알고리즘)
# 4 11
# 802
# 743
# 457
# 539


def countCheck(len):
    cnt = 0
    for x in line:
        cnt += x//len
    return cnt


k, n = map(int, input().split())
line = []

for i in range(k):
    line.append(int(input()))


ret = 0
lt = 0
rt = max(line)

while lt <= rt:
    mid = (lt + rt) // 2

    if countCheck(mid) >= n:
        ret = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ret)