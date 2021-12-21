# 3. 뮤직비디오(결정알고리즘)
# 9 9
# 1 2 3 4 5 6 7 8 9

# 9곡을 3장 DVD에 담기.

n, m = map(int, input().split())
music = list(map(int, input().split()))


def countCheck(capacity):
    cnt = 1
    sum = 0
    for x in music:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt


lt = 0
rt = sum(music)
ret = 0
maxx = max(music)

while lt <= rt:
    mid = (lt + rt) // 2

    if mid >= maxx and countCheck(mid) <= m:
        ret = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(ret)
