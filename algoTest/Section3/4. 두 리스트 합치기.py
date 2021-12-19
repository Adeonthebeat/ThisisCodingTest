# 4. 두 리스트 합치기
# 3
# 1 3 5
# 5
# 2 3 6 7 9

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = []

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

if p1 < n:
    c = c + a[p1:]
else:
    c = c + b[p2:]

for i in c:
    print(i, end=' ')

# arr = arr_1 + arr_2
# arr_1.extend(arr_2)

# for i in sorted(arr):
#     print(i, end= ' ')
