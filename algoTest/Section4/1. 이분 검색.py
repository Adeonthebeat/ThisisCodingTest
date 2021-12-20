
# 1. 이분 검색
# 8 32
# 23 87 65 12 57 32 99 81
# 30 57
# 6 32 38 1 28 76 51 8 98 88 74 60 65 57 97 63 56 99 85 5 13 100 61 36 44 50 62 41 91 9

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

lt = 0
rt = n - 1

while lt <= rt:
    mid = (lt + rt) // 2
    if arr[mid] == m:
        print(mid+1)
        break
    elif arr[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1



