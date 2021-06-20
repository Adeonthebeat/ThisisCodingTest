'''
# 정렬 알고리즘
선택 정렬 
 - 가장 작은 데이터를 '선택'해서 정렬되지 않은 데이터 중에서 가장 앞쪽에 있는 데이터와 위치를 바꾸는 방법
 - 아이디어가 가장 간단한 알고리즘
 - 평균시간 알고리즘 = O(N2)
 - 공간복잡도 = O(N)
삽입 정렬
 - 데이터를 앞에서부터 하나씩 확인하며, 데이터를 적절한 위치에 '삽입'하는 방법
 - 데이터가 거의 정렬되어 있을 때, 가장 빠른 알고리즘
 - 평균시간 알고리즘 = O(N2)
 - 공간복잡도 = O(N)
퀵 정렬
 - 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
 - 대부분의 경우에 가장 적합하며 빠른 알고리즘
 - 평균시간 알고리즘 = O(NlogN)
 - 공간복잡도 = O(N)
계수 정렬
 - 특정한 값을 가지는 데이터의 개수를 '카운트'하는 방법
 - 데이터의 크기가 한정되어 있는 경우에만 사용가능하지만, 매우 빠른 알고리즘
 - 평균시간 알고리즘 = O(N + K)
 - 공간복잡도 = O(N + K)
'''
import heapq

'''
# 국영수 문제
 - 국어점수가 감소하는 순서대로
 - 국어점수가 같으면, 영어점수가 증가하는대로
 - 국어점수와 영어점수가 같으면, 수학점수가 감소하는대로
 - 모든 점수가 같으면 사전 순으로 증가하는 순으로(아스키코드에서는 대문자는 소문자보다 작으므로 사전 순으로 앞에 옴)

# Developer`s Kick!
 - .sort(key=lambda x: ())

Input01
12
Junkyu 50 60 100
Sankeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

Output01
Donghyuk
Sankeun
Sunyoung
nsj
Wonseob
Sanghyun
Sei
Kangsoo
Haebin
Junkyu
Soong
Taewhan
'''


def korean_English_Math():
    n = int(input())

    # 학생 정보를 담을 리스트
    students = []

    # 모든 학생 정보 입력받기
    for _ in range(n):
        students.append(input().split())
    '''
    [정렬기준]
    1) 두 번째 원소를 기준으로 내림차순 정렬
    2) 두 번째 원소가 같다면, 세 번째 원소를 기준으로 오름차순 정렬
    3) 세 번째 원소가 같다면, 네 번째 원소를 기준으로 내림차순 정렬
    4) 네 번째 원소가 같다면, 첫 번째 원소를 기준으로 오름차순 정렬
    '''
    students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

    # 정렬된 학생 정보에서 이름만 출력
    for student in students:
        print(student[0])


'''
# 안테나 문제
 - 모든 집까지의 거리의 총합이 최소가 되는 위치
 
# Developer`s Kick!
 - 중간값(Median)에 해당하는 위치의 집에 안테나를 설치 -> 모든 집까지의 거리가 최소가 됨

Input01
4
5 1 7 9

Output01
5
'''


def antena():
    n = int(input())
    data = list(map(int, input().split()))
    data.sort()

    # 중간값(Median)을 출력
    print(data[(n - 1) // 2])


'''
# 실패율 문제
 - 실패율 : 스테이지에 도달했으나, 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
 - N : 전체 스테이지의 개수
 - stages : 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
 - 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담긴 배열 return
# Developer`s Kick!
 - 스테이지 번호(i)를 1부터 N까지 증가시키며, 해당 단계에 머물러 있는 플레이어 수(count)를 계산
 - 플레이어 수(count)를 이용하여 모든 스테이지의 실패율을 계산한 뒤, 저장
 - 실패율이 높은 스테이지부터 내림차순
'''


def fail_ratio(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물어 있는 사람의 수 계산
        count = stages.count(i)

        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length

        # 리스트에 (스테이지번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이즈를 내림차순으로 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse=True)

    # 정렬된 스테이지 번호 출력
    answer = [i[0] for i in answer]
    return answer


'''
# 카드 정렬하기 문제
 - N개의 카드 묶음이 주어졌을 때, 최소 비교방법
# Developer`s Kick!
 - 항상 가장 작은 크기의 두 카드 묶음을 합쳤을 때, 최적의 해를 구함

Input01
3
10
20
40

Output01
100
 
'''


def card_Sort():

    n = int(input())

    # 힙(Heap)에서 초기 카드 묶음을 모두 삽입
    heap = []
    for i in range(n):
        data = int(input())
        heapq.heappush(heap, data)

    ret = 0

    # 힙(Heap)에 원소가 1개 남을 때까지
    while len(heap) != 1:
        # 가장 작은 2개의 카드 묶음 꺼내기
        one = heapq.heappop(heap)
        two = heapq.heappop(heap)

        # 카드 묶음을 합쳐서 다시 묶음
        sum_value = one + two
        ret += sum_value
        heapq.heappush(heap, sum_value)

    print(ret)


if __name__ == "__main__":
    # korean_English_Math()
    # antena()
    # fail_ratio()
    card_Sort()
