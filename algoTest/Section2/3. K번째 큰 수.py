

# 10 3
# 13 15 34 23 45 65 33 11 26 42
T, k = map(int, input().split())
arr = list(map(int, input().split()))

res = set()
for i in range(T):
    for j in range(i+1, T):
        for m in range(j+1, T):
            res.add(arr[i] + arr[j] + arr[m])

res = list(res)
res.sort(reverse=True)
print(res[k-1])
