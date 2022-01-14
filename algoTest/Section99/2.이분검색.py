# 8 32
# 23 87 65 12 57 32 99 81
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()


lt = 0
rt = n - 1
while lt <= rt:
    mid = (lt + rt)//2

    if arr[mid] == m:
        print(mid+1)
        break
    elif arr[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1

