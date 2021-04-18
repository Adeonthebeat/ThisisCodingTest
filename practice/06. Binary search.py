# 이진탐색 : 탐색범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
# 이진탐색은 배열 내부의 데이터가 정렬되어 있어 있어야만 사용할 수 있는 알고리즘
# 이진탐색은 범위의 시작점, 끝점, 중간점이 있으며, 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교하여 원하는 데이터를 찾음 
# 이진탐색은 코드를 다양한 문제를 접하면서 가급적 외우길 권함

# 순차탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법

# 트리구조 : 노드와 노드의 연결로 표현하며, 노드는 정보의 단위로 어떠한 정보를 가지고 있는 개체
# 트리구조의 예는 데이터베이스
# 트리구조의 특징
# 1. 트리는 부모 노드와 자식 노드의 관계로 표현
# 2. 트리의 최상단노드를 루트 노드라 함
# 3. 트리의 최하단노드를 단말 노드라 함
# 4. 트리에서 일부르,ㄹ 뗴어내도 트리구조이며, 이를 서브 구조라고 함
# 5. 트리구조는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합

# 이진 탐색 트리 : 가장 간단한 트리구조
# 왼쪽 자식노드 < 부모 노드 < 오른쪽 자식 노드 식으로 구성

# 파라메트릭 서치 : 최적화 문제를 결정 문제로 바꾸어 해결하는 기법
# 원하는 조건에 만족하는 가장 알맞을 값을 찾는 문제

import sys


# 순차탐색
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1  # 현재의 위치 반환

    return ""


# 이진탐색 : 배열 내부의 데이터가 정렬되어 있어 있어야만 사용할 수 있는 알고리즘
# 재귀함수 사용 
def binary_search_recursive(array, target, start, end):
    # 시작점이 끝점보다 크다면, 리턴
    if start > end:
        return

    # 중간 인덱스 설정 - 개발자의 킥!
    mid = (start + end) // 2

    ## 재귀함수를 통한 이진탐색!
    # 중간 인덱스 반환
    if array[mid] == target:
        return mid

    # 찾으려는 값이 중간 값보다 작다면, 왼쪽부터 Search
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid - 1)

    # 찾으려는 값이 중간 값보다 크다면, 오른쪽부터 Search
    else:
        return binary_search_recursive(array, target, mid + 1, end)


# 이진탐색 : 배열 내부의 데이터가 정렬되어 있어 있어야만 사용할 수 있는 알고리즘
# 루프만 사용
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


# 빠르게 입력받기 - 시간초과 문제 해결
def readline_practice():
    # 하나의 문자열 데이터 입력받기
    ret = sys.stdin.readline().rstrip()

    # print(ret) # 출력
    return ret


# 부품찾기
# 이진탐색
def find_part_binary(array, target, start, end):
    while start <= end:

        mid = (start + end) // 2

        if array[mid] == target:
            return mid

        elif array[mid] > target:
            end = mid - 1

        else:
            start = mid + 1

    return None


# 부품찾기
# 계수정렬
def find_part_count_sort():
    # 5
    # 8, 3, 7, 9, 2
    # 3
    # 5, 7, 9

    n = int(input())
    array = [0] * 1000001

    for i in input().split(','):
        array[int(i)] = 1

    m = int(input())
    x = list(map(int, input().split(',')))

    for i in x:
        if array[i] == 1:
            print("yes", end=' ')
        else:
            print("no", end=' ')

    return ""


# 부품찾기
# 집합자료형
def find_part_lib():
    # 5
    # 8, 3, 7, 9, 2
    # 3
    # 5, 7, 9
    n = int(input())
    array = set(map(int, input().split(',')))

    m = int(input())
    x = list(map(int, input().split(',')))

    # 요구 부품번호 하나씩 아웃
    for i in x:
        if i in array:
            print("yes", end=' ')
        else:
            print("no", end=' ')

    return ""


# 떡볶이 떡 만들기( 파라메트릭 서치 )
# 떡의 개수 n, 떡의 길이 m
# 각 떡의 높이 = 리스트
# M 만큼 떡을 가져갈 수 있는 최대 높이(많이) = Output
def make_dduck():
# 4 6
# 19 15 10 17
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    start = 0
    end = max(array)

    ret = 0
    while start <= end:
        total = 0
        mid = (start + end)//2

        for x in array:
            # 잘랐을 때, 떡의 양 계산
            if x > mid:
                total += x - mid
        # 떡이 부족한 경우, 더 많이 자르기(왼쪽)
        if total < m:
            end = mid - 1
        # 떡이 많으면 덜 자르기(오른쪽)
        else:
            ret = mid # 최대한 덜 잘랐을 때, 떡의 나머지 높이가 커지므로 정답!
            start = mid + 1

    return ret

def find_digit(array, target, start, end):

    if start > end:
        return

    while start <= end:

        mid = (start + end)//2

        if array[mid] == target:
            return True
        elif array[mid] > mid:
            find_digit(array, target, start, mid - 1)
        else:
            find_digit(array, target,  mid + 1, mid - 1)

    return None





if __name__ == "__main__":
    ####################################################################

    # print("생성할 원소 개수를 입력한 후, 한칸 띄고 찾을 문자열을 입력하시오.")
    # data = input().split()
    # n = int(data[0])
    # target = data[1]

    # print("원소의 개수만큼 문자를 입력하시오")
    # array = input().split()

    # print(sequential_search(n, target, array))

    ####################################################################

    # 원소의 개수, 찾고자하는 문자열
    # n, target = 10, 7
    # array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # # array = [1, 3, 5, 6, 9, 11, 13, 15, 17, 19]
    # # ret = binary_search_recursive(array, target, 0, n-1)
    # ret = binary_search(array, target, 0, n-1)
    # if ret is None:
    #     print("원소가 존재하지 않습니다.")
    # else:
    #     print(ret + 1)

    ####################################################################

    # print(readline_practice())

    ####################################################################

    # 부품점
    # n = int(input()) # 부품 개수
    # array = list(map(int, input().split())) # 목록 리스트업
    # n = 5  # 부품 개수
    # array = [8, 3, 7, 9, 2]
    # array.sort()

    # 고객 요구사항
    # m = int(input()) # 요구 부품 개수
    # x = list(map(int, input().split()))  # 요구 목록 리스트업
    # m = 3
    # x = [5, 7, 9]

    ## 이진탐색
    # for i in x:
    #     ret = find_part_binary(array, i, 0, n - 1)
    #     if ret is not None:
    #         # print("부품이 없슴다~")
    #         print("yes", end=' ')
    #     else:
    #         print("no", end=' ')
    #         # print("%s 개 있슴다~ " %(ret + 1))
    ####################################################################

    ## 계수정렬
    # print(find_part_count_sort())

    # 라이브러리 사용
    # print(find_part_lib())
    # print(make_dduck())

    n = int(input())
    array = sorted(list(map(int, sys.stdin.readline().split())))

    m = int(input())
    x = list(map(int, sys.stdin.readline().split()))

    for i in x:
        ret = find_digit(array, i, 0, n - 1)
        if ret is not None:
            print(1)
        else:
            print(0)