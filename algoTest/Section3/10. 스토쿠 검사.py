# 10. 스도쿠 검사
# 9 6 1 8 2 5 3 7 4
# 2 8 3 1 7 4 5 6 9
# 5 4 7 3 6 9 1 2 8
# 1 2 8 9 3 6 7 4 5
# 3 7 5 4 8 1 6 9 2
# 6 9 4 2 5 7 8 1 3
# 8 1 2 7 4 3 9 5 6
# 7 3 6 5 9 2 4 8 1
# 4 5 9 6 1 8 2 3 7

def check(arr):
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[arr[i][j]] = 1  # 행 체크
            ch2[arr[j][i]] = 1  # 열 체크

        # 합이 9가 아니라면, False
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False

    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[arr[i * 3 + k][j * 3 + s]] = 1
            if sum(ch3) != 9:
                return False
    return True


arr = [list(map(int, input().split())) for _ in range(9)]

if check(arr):
    print("YES")
else:
    print("NO")
