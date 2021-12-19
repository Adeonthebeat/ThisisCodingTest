
# 2. 숫자만 추출
# g0en2Ts8eSoft

text = input()
'''
num = ''
for i in text:
    if i.isnumeric():
        num += i

ret = int(num)
cnt = 0
for i in range(1, ret+1):
    if ret % i == 0:
        cnt += 1

print(ret)
print(cnt)
'''

res = 0
for x in text:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)