
# 8. 단어 찾기
# 5
# big
# good
# sky
# blue
# mouse
# sky
# good
# mouse
# big

n = int(input())
p = dict()

for i in range(n):
    text = input()
    p[text] = 1

for j in range(n-1):
    text = input()
    p[text] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break