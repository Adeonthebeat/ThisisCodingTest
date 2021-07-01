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
            dp.append(array[index:index+m])
            index += m

        # 다이나믹 프로그래밍 진행
        for j in range(1, m):
            for i in range(n):
                # 왼쪽 위에서 오는 경우
                if i == 0:
                    left_up = 0
                else:
                    left_up = dp[i-1][j-1]

                # 왼쪽 아래에서 오는 경우
                if i == n - 1:
                    left_down = 0
                else:
                    left_down = dp[i+1][j-1]

                # 왼쪽에서 오는 경우
                left = dp[i][j-1]

                dp[i][j] = dp[i][j] + max(left_up, left_down, left)

        ret = 0
        for i in range(n):
            ret = max(ret, dp[i][m-1])

        print(ret)


if __name__ == "__main__":
    gold_mime()
