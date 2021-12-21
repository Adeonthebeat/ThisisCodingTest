
# 9. 증가 수열 만들기(그리디)
# 5
# 2 4 5 1 3

n= int(input())
arr = list(map(int, input().split()))

lt = 0
rt = n-1
last = 0
ret = ""
tempList = []

while lt <= rt:
    if arr[lt] > last:
        tempList.append((arr[lt], 'L'))
    if arr[rt] > last:
        tempList.append((arr[rt], 'R'))
    tempList.sort()
    if len(tempList) == 0:
        break
    else:
        ret = ret + tempList[0][1]
        last = tempList[0][0]
        if tempList[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tempList.clear()

print(len(ret))
print(ret)