
# 후위표기식 만들기
# 3+5*2/(7-2)
# 3*(5+2)-9

n = input()
stack = []
ret = ''

for i in n:
    if i.isdecimal():
        ret += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ret += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                ret += stack.pop()
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                ret += stack.pop()
            stack.pop()
while stack:
    ret += stack.pop()

print(ret)