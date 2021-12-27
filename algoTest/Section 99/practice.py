# 숫자만 추출

def cntYak(x):
    cnt = 0
    for i in range(1, x+1):
        if x % i == 0:
            cnt += 1
    return cnt

texts = input()
ret = ""

for text in texts:
    if text.isnumeric():
        ret += text

print(int(ret))
print(cntYak(int(ret)))