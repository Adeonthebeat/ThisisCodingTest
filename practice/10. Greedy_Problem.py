
'''
# 모험가 길드 문제
모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로
구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했다.
N명의 모험가에 대한 정보가 주어졌을때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하라.

# Developer`s Kick!
공포도가 낮을 수록 그룹을 짜기 쉽기 때문에 오름차순으로 정렬을 해준다. 그 후 모든 모험가들을 차례대로 검사한다.
현재 모험가의 공포도가 그룹인원보다 높다면 그룹인원에 추가하고 다음 모험가를 탐색한다.
현재 모험가의 공포도가 그룹인원과 같다면 그룹과 여행을 떠난다.
그리고 다음 모험가를 탐색하며 새로운 그룹을 만든다. 이를 반복하면서 구하면 된다.

# Input
5
2 3 1 2 2
'''
import heapq


def adventurer_Guild():
    # 모험가의 수
    n = int(input())
    # n = 5

    # 공포도의 값 리스트
    data = list(map(int, input().split()))
    # data = [2, 3, 1, 2, 2]
    data.sort()

    # 총 그룹의 수
    result = 0

    # 현재 그룹에 포함된 모험가의 수
    cnt = 0

    # for문
    for i in data:
        # 현재 그룹에 해당 모험가를 포함
        cnt += 1

        # 현재 그룹에 해당 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
        if cnt >= i:
            # 총 그룹 수 증가
            result += 1

            # 현재 그룹에 포함된 모험가의 수 초기화
            cnt = 0

    print(result)
'''
# 곱하기 혹은 더하기 문제
각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+'연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
단, +보다 X를 먼저 계산하는 일반적인 방식과는 달리,
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

* Developer`s Kick!
문자열에서 제일 좌측에 있는 수를 ret으로 지정하고 오른쪽으로 한개씩 연산한 후 그 값을 ret으로 바꿈
ret와 오른쪽 숫자 하나씩 비교해서, 1이하인 수가 있으면 더하기연산

# Input
02984
567
'''
def multiply_plus():
    data = input()

    ret = int(data[0])

    for i in range(1, len(data)):
        num = int(data[i])
        if num <= 1 or ret <= 1:
            ret += num
        else:
            ret *= num
    print(ret)


'''
# 문자열 뒤집기
다솜이는 0과 1로만 이루어진 문자열 S를 가지고 있습니다. 다솜이는 이 문자열 S에 있는 모든 숫자를 전부 같게 만들려고 합니다. 다솜이 할 수 있는 행동은 S에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것입니다.
예를 들어 S = 0001100일 때는 다음과 같습니다.
1. 전체를 뒤집으면 1110011이 된다.
2. 4번째 문자무터 5번째 문자까지 뒤집으면 1111111이 되어서 두번만에 모두 같은 숫자로 만들 수 있다.
하지만, 처음부터 4, 5번째 문자를 뒤집었으면 한번에 0000000이 되어서 1번만에 모두 같은 숫자로 만들 수 있습니다.

* Developer`s Kick!
전부 0으로 바뀌는 경우와 전부 1로 바뀌는 경우 중에서 더 적은 횟수를 가지는 경우를 계산 해야한다.

# Input : 0001100
'''
def flip_String():
    data = input()

    cnt00 = 0   # 전부 0
    cnt01 = 0   # 전부 1

    if data[0] == '1':
        cnt00 += 1
    else:
        cnt01 += 1

    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            if data[i+1] == '1':
                cnt00 += 1
            else:
                cnt01 += 1
    print(min(cnt00, cnt01))

'''
# 만들 수 없는 금액
문제
동네 편의점의 주인인 아뎅은 N개의 동전을 가지고 있습니다. 
이때 N개의 동전을 이용하여 만들수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.

입력조건
- 첫째 줄에는 동전의 개수를 나타내는 양의 정수 N이 주어집니다. (1 <= N <= 1,000)
- 둘째 줄에는 각 동전의 화폐 단위를 나타내는 N개의 자연수가 주어지며, 각 자연수는 공백으로 구분합니다. 이때, 각 화폐 단위는 1,000,000 이하의 자연수 입니다.
출력조건
- 첫째 줄에 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값을 출력합니다.

* Developer`s Kick!
제일 작은 수부터 비교하기 위해 양의 정수 리스트를 오름차순으로 정렬한다.
target을 1로 설정한다.
target 이 가지고 있는 동전 리스트 중 어떤 수보다 작은 수이면 그 아래 수까지 만들 수 있는 것이다.

# Input
5
3 2 1 1 9
'''
def Uncreateable_Amount():
    
    # 동전의 개수
    n = int(input())
    
    # 동전의 리스트 입력
    data = list(map(int, input().split()))

    # 제일 작은 수부터 비교하기 위해 양의 정수 리스트를 오름차순으로 정렬한다.
    data.sort()

    # target을 1로 설정한다.
    # target이 가지고 있는 동전 리스트 중 어떤 수보다 작은 수라면, 그 아래 수까지 만들 수 있는 것이다.
    target = 1
    for i in data:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        if target < i:
            break
        else:
            target += i
    print(target)


'''
# 볼링공 고르기
A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다. 
볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다. 
또한 같은 무게의 공이 여러개 있을 수 있지만, 서로 다른 공을 갖는다고 간주합니다. 
볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.
N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

# 입력조건
첫째 줄에 볼링공의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.
(1 <= N <= 1,000, 1 <= M <= 10)
둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.
(1 <= K <= M)

# 출력조건
첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.

* Developer`s Kick!
각 무게의 볼링공이 몇개인지 파악하는 것!

# Input : 
5 3
1 3 2 3 2
8 5
1 5 4 3 2 4 5 2
'''
def Choose_BowlingBall():
    
    # 볼링공의 개수, 공의 최대무게
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # 1 ~ 10의 무게를 담을 수 있는 리스트
    arr = [0] * 11

    for x in data:
        # 각 무게에 해당하는 볼링공의 개수 카운트
        arr[x] += 1

    ret = 0
    # 1부터 m까지의 각 무게에 대하여 처리
    for i in range(1, m):
        n -= arr[i]         # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
        ret += arr[i] * n   # B가 선택하는 경우의 수와 곱해주기
    print(ret)


'''
# 무지의 먹방 라이브
평소 식욕이 왕성한 무지는 자신의 재능을 뽐내고 싶어 졌고 고민 끝에 카카오 TV 라이브로 방송을 하기로 마음먹었다.

그냥 먹방을 하면 다른 방송과 차별성이 없기 때문에 무지는 아래와 같이 독특한 방식을 생각해냈다.

회전판에 먹어야 할 N 개의 음식이 있다.
각 음식에는 1부터 N 까지 번호가 붙어있으며, 각 음식을 섭취하는데 일정 시간이 소요된다.
무지는 다음과 같은 방법으로 음식을 섭취한다.

무지는 1번 음식부터 먹기 시작하며, 회전판은 번호가 증가하는 순서대로 음식을 무지 앞으로 가져다 놓는다.
마지막 번호의 음식을 섭취한 후에는 회전판에 의해 다시 1번 음식이 무지 앞으로 온다.
무지는 음식 하나를 1초 동안 섭취한 후 남은 음식은 그대로 두고, 다음 음식을 섭취한다.
다음 음식이란, 아직 남은 음식 중 다음으로 섭취해야 할 가장 가까운 번호의 음식을 말한다.
회전판이 다음 음식을 무지 앞으로 가져오는데 걸리는 시간은 없다고 가정한다.
무지가 먹방을 시작한 지 K 초 후에 네트워크 장애로 인해 방송이 잠시 중단되었다.
무지는 네트워크 정상화 후 다시 방송을 이어갈 때, 몇 번 음식부터 섭취해야 하는지를 알고자 한다.
각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열 food_times, 네트워크 장애가 발생한 시간 K 초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return 하도록 solution 함수를 완성하라.

# 제한사항
food_times 는 각 음식을 모두 먹는데 필요한 시간이 음식의 번호 순서대로 들어있는 배열이다.
k 는 방송이 중단된 시간을 나타낸다.
만약 더 섭취해야 할 음식이 없다면 -1을 반환하면 된다.
정확성 테스트 제한 사항
food_times 의 길이는 1 이상 2,000 이하이다.
food_times 의 원소는 1 이상 1,000 이하의 자연수이다.
k는 1 이상 2,000,000 이하의 자연수이다.
효율성 테스트 제한 사항
food_times 의 길이는 1 이상 200,000 이하이다.
food_times 의 원소는 1 이상 100,000,000 이하의 자연수이다.
k는 1 이상 2 x 10^13 이하의 자연수이다.

* Developer`s Kick!
시간이 적게 걸리는 음식부터 확인하는 그리디 알고리즘
모든 음식을 시간을 기준으로 정렬 후, 적게 걸리는 음식부터 제거하는 방식을 이용
-> 우선순위 큐 heapq 라이브러리 이용
'''

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면, -1
    if sum(food_times) <= k:
        return -1

    # 시간이 적게 드는 음식부터 먹어야 하므로, 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        # (음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i+1))

    # 먹기 위해 사용한 시간
    sum_value = 0

    # 직전에 다 먹은 음식 시간
    previous = 0

    # 남은 음식의 개수
    length = len(food_times)

    # sum_value + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length

        # 다 먹은 음식 제외
        length -= 1

        # 이전 음식 시간 재설정
        previous = now

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    ret = sorted(q, key=lambda x: x[1]) # 음식 번호 기준으로 정렬
    return ret[(k - sum_value) % length][1]

if __name__ == "__main__":
    # adventurer_Guild()
    # multiply_plus()
    # flip_String()
    # Uncreateable_Amount()
    Choose_BowlingBall()