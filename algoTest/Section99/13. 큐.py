from collections import deque
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA
text = input()
n = int(input())

for i in range(n):
    plan = input()
    Q = deque(text)

    for x in plan:
        if x in Q:
            if x != Q.popleft():
                print("NO")
                break
    else:
        if len(Q) == 0:
            print("YES")
        else:
            print("NO")