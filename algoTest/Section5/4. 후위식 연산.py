
# 후위식 연산
# 352+*9-

n = input()
stack = []

for x in n:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n2 = stack.pop()
            n1 = stack.pop()
            stack.append(n2+n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2-n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2*n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)

print(stack[0])