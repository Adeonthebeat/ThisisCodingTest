
# 회문 문자열 검사
# 5
# level
# moon
# abcba
# soon
# gooG

n = int(input())

for i in range(n):
    text = input().upper()
    size = len(text)

    for j in range(size):
        if text[j] != text[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))

    # print("#%d YES" %(i + 1)) if text == text[::-1] else print("#%d NO" % (i + 1))
