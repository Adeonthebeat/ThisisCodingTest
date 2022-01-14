# 9 3
# 1 2 3 4 5 6 7 8 9
n, m = map(int, input().split())
music = list(map(int, input().split()))
music.sort()

def cntCheck(capacity):
    cnt = 1
    summ = 0
    for x in music:
        if summ + x > capacity:
            cnt += 1
            summ = x
        else:
            summ += x
    return cnt

lt = 0
rt = sum(music)
ret = 0
maxx = max(music)

while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= maxx and cntCheck(mid) <= m:
        ret = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(ret)