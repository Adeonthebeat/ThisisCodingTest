
# 1. 가장 큰 수 (스택)
# 5276823 3
# 9977252641 5

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    # stack 비어 있지 않으면.
    while stack and m > 0 and stack[-1] < x:
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

ret = ''.join(map(str, stack))
print(ret)



