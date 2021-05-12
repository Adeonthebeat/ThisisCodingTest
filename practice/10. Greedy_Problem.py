
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
    print(target)



if __name__ == "__main__":
    # adventurer_Guild()
    # multiply_plus()
    # flip_String()
    Uncreateable_Amount()