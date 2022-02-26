

T = int(input())
odds = 0
test_list = []
for test_case in range(1, T + 1):
    temp = map(int, input().split())
    for x in temp:
        if x % 2 != 0:
            odds += x
    test_list.append(odds)

for i in range(len(test_list)):
    print("#", i, test_list[i])
