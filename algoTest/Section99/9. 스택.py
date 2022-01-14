# 가장 큰 수
# 5276823 3
# 9977252641 5
num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []


for x in num:
    print('xx', x)
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

print(''.join(map(str, stack)))





