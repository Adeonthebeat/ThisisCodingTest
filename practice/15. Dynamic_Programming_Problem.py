'''
# 다이나믹 프로그래밍
 - 한 번 해결된 부분 문제의 정답을 메모리에 기록하여, 한 번 계산한 답은 다시 계산하지 않도록 하는 문제해결기법
 - 점화식 : 인접한 항들 사이의 관계식을 의미
 - 다이나믹 프로그래밍은 점화식으로 그대로 코드로 옮겨서 구현
 예) 피보나치 수열
 - Top_down VS Bottom_up
  - Top_down : 재귀함수를 이용하여 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식
  - Bottom_up: 단순히 반복문을 이용하여 작은 문제를 먼저 해결하고, 해결된 작은 문제를 모아 큰 문제를 해결하는 방식
'''

'''
# 금광 문제 
 - N X M 크기의 금광이 존재하며, 최대의 금을 캐는 값을 구하시오.

# Developer`s Kick!
 - 맨 왼쪽열을 고정시키고 1) 왼쪽 위에서 오는 경우 2) 왼쪽에서 오는 경우 3) 왼쪽 아래에서 오는 경우를 계산.
 - 점화식 : dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1])

Input01
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

Output01 
19
16

'''


def gold_mime():
    # 테스트 케이스( Test Case ) 입력
    for tc in range(int(input())):
        # 금광 정보 입력
        n, m = map(int, input().split())
        array = list(map(int, input().split()))

        # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화 - 와꾸
        dp = []
        index = 0
        for i in range(n):
            dp.append(array[index:index + m])
            index += m

        # 다이나믹 프로그래밍 진행
        for j in range(1, m):
            for i in range(n):
                # 왼쪽 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = dp[i - 1][j - 1]

                # 왼쪽 아래에서 오는 경우
                if i == n - 1:
                    left_down = 0
                else:
                    left_down = dp[i + 1][j - 1]

                # 왼쪽에서 오는 경우
                left = dp[i][j - 1]

                dp[i][j] = dp[i][j] + max(left_up, left_down, left)

        ret = 0
        for i in range(n):
            ret = max(ret, dp[i][m - 1])

        print(ret)


'''
# 정수삼각형 문제
 - 크기가 5인 삼각형을 내려오면서 최대 값을 구하시오.

# Developer`s Kick!
 - 1) 왼쪽 위 2) 바로 위 위체서만 내려올 수 있음
 - 모든 위치를 기준으로 이전 우치로 가능한 위치까지의 최적의 합 중 더 큰 합을 가지는 경우를 선택
 - dp[i][j] = array[i][j] + max(dp[i-1][j-1], dp[i-1][j]) 
 
Input01
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

Output01 
30

'''


def triangle():
    n = int(input())

    # 다이나믹 프로그래밍을 위한 DP 테이블 초기화
    dp = []

    for _ in range(n):
        dp.append(list(map(int, input().split())))

    # 다이나믹 프로그래밍으로 두 번째 줄부터 내려가면서 확인
    for i in range(1, n):
        for j in range(i + 1):
            # 왼쪽 위에서 내려오는 경우
            if j == 0:
                up_left = 0
            else:
                up_left = dp[i - 1][j - 1]
            # 바로 위에서 내려오는 경우
            if j == i:
                up = 0
            else:
                up = dp[i - 1][j]
            # 최대 합 저장
            dp[i][j] = dp[i][j] + max(up_left, up)

    print(max(dp[n - 1]))


'''
# 퇴사 문제 
 - 퇴사하기 전 얻을 수 있는 최대 수익을 구하시오.
# Developer`s Kick!
 - 뒤쪽 매 상담에 대하여 '현재 상담일자의 이윤(p[i]) + 현재 상담을 마친 일자로부터의 최대 이윤(dp[t[i]+i])을 계산
 - dp[i] = max(p[i] + dp[t[i]+i], max_value)
 - max_value = 뒤에서부터 계산할 때, 현재까지의 최대 상담금액에 해당하는 변수

Input01
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

Output01  
45

Input02
10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

Output02  
55

'''


def resignation():
    n = int(input())  # 전체 상담 개수
    t = []  # 각 상담을 완료하는데 걸리는 시간
    p = []  # 각 상담을 완료했을 때, 받을 수 있는 금액
    dp = [0] * (n + 1)  # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
    max_value = 0  # 뒤에서부터 계산할 때, 현재까지의 최대 상담금액에 해당하는 변수

    for _ in range(n):
        x, y = map(int, input().split())
        t.append(x)
        p.append(y)

    # 리스트를 뒤에서부터 거꾸로 확인
    for i in range(n - 1, -1, -1):
        time = t[i] + i

        # 상담이 기간안에 끝나는 경우
        if time <= n:
            # 점화식
            dp[i] = max(p[i] + dp[time], max_value)
            max_value = dp[i]
        else:
            dp[i] = max_value

    print(max_value)


'''
# 병사 배치하기 문제
 - N명의 병사가 무작위로 나열
 - 각 병사는 전투력을 보유하고 있으며, 전투력이 높은 순으로 내림차순으로 배치
 - 즉, 앞의 병사의 전투력이 뒤 병사의 전투력보다 높아야 함
 - 남아 있는 병사의 수가 최대가 되도록 하시오. 
# Developer`s Kick!
 - 가장 긴 증가하는 부분 수열 문제: 하나의 수열이 주어졌을 때, 값이 증가하는 형태의 가장 긴 부분 수열을 찾는 문제
 arr = {10, 20, 10, 30, 20, 50} => {10, 20, 30, 50}
 - D[i] = arr[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
 - 점화식 : D[i] = max(D[i], D[j] + 1) if arr[j] < arr[i] 

Input01
7
15 11 4 8 5 2 4

Output01  
2
'''


def soldier():
    n = int(input())
    array = list(map(int, input().split()))

    # 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
    array.reverse()

    # 다이나믹 프로그래밍을 위한 1차원 DP 테이블
    dp = [1] * n

    # 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
    for i in range(1, n):
        for j in range(0, i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    # 열외시켜줘야 하는 병사의 최소수를 출력
    print(n - max(dp))


'''
# 못생긴 수 문제
 - 소인수로 가지는 수( 2, 3, 5 )
 - 1을 포함 
# Developer`s Kick!
 - 2의 배수, 3의 배수, 5의 배수 = 못생긴 수

Input01
10

Output01
12 

Input02
4

Output02
4

'''


def ugly_number():
    n = int(input())

    # 못생긴 수를 담기 위한 DP 테이블
    ugly = [0] * n

    # 첫 번째 못생긴 수는 1
    ugly[0] = 1

    # 2배, 3배, 5배를 위한 인덱스
    i2 = i3 = i5 = 0

    # 처음에 곱셉값을 초기화
    next2, next3, next5 = 2, 3, 5

    # 1부터 n까지의 못생긴 수 찾기
    for i in range(1, n):

        # 가능한 곱셉 결과 중에서 가장 작은 수 선택.
        ugly[i] = min(next2, next3, next5)

        # 인덱스에 따라 곱셉 결과 증가
        if ugly[i] == next2:
            i2 += 1
            next2 = ugly[i2] * 2
        if ugly[i] == next3:
            i3 += 1
            next3 = ugly[i3] * 3
        if ugly[i] == next5:
            i5 += 1
            next5 = ugly[i5] * 5

    print(ugly[n - 1])


if __name__ == "__main__":
    # gold_mime()
    # triangle()
    # resignation()
    # soldier()
    ugly_number()
