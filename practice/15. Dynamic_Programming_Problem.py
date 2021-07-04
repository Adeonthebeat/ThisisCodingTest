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


if __name__ == "__main__":
    # gold_mime()
    # triangle()
    resignation()
