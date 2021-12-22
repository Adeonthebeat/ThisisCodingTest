
# 10. 역수열(그리디)
# 8
# 5 3 4 0 2 1 1 0

n = int(input())
arr = list(map(int, input().split()))
seq = [0] * n
for i in range(n):
    for j in range(n):
        # arr[i] == 0 본인보다 큰 숫자가 들어갈 앞자리 확보,
        # seq 빈자리 체크 (이미 차있는지 확인)
        if arr[i] == 0 and seq[j] == 0:
            seq[j] = i + 1 # 본인 자리에 인덱스 넣기.
            break
        elif seq[j] == 0:
            arr[i] -= 1

for x in seq:
    print(x, end=' ')
