from collections import deque
# 7. 교육과정설계(큐)
# CBA
# 3
# CBDAGE
# FGCDAB
# CTSBDEA

# AFC
# 1
# AFFDCCFF

need = input()
n = int(input())

for i in range(n):
    plan = input()
    dq = deque(need)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" % (i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" % (i + 1))
        else:
            print("#%d NO" % (i + 1))