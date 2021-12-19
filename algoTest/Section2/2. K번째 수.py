import sys
import os

# 2
# 6 2 5 3
# 5 2 7 3 8 9
# 15 3 10 3
# 4 15 8 16 6 6 17 3 10 11 18 7 14 7 15

T = int(input())

for t in range(T):
    n, s, e, k = map(int, input().split())
    arrList = list(map(int, input().split()))

    arr = arrList[s-1:e]
    arr.sort()
    print("# %d %d" %(t-1, arr[k-1]))
    
    
