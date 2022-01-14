# 4 11
# 802
# 743
# 457
# 539

def cntCheck(ct):
    cnt = 0
    for x in line:
        cnt += x // ct
    return cnt


n, m = map(int, input().split())
line = []

for _ in range(n):
    line.append(int(input()))

lt = 0
rt = max(line)
ret = 0

while lt <= rt:
    mid = (lt + rt) // 2

    if cntCheck(mid) >= m:
        ret = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(ret)