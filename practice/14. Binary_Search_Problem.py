'''
[이진탐색 알고리즘]
탐색범위를 반으로 줄여나가면서 데이터를 빠르게 탐색하는 기법
이진탐색은 배열 내부의 데이타 정렬되어 있을 때만 사용할 수 있음
이진탐색 알고리즘에서는 3가지 변수 사용 ( 시작점, 끝점, 중간점 )
시작점, 끝점은 탐색하고자 하는 범위를 나타내기 위해 사용하며, 탐색범위의 중간점에 있는 테이터와 찾고자 하는 데이터를 비교

[bisect 클래스]
단순히 정렬된 배열에서 특정한 데이터를 찾도록 요구하는 문제에서는
이진탐색을 직접 구현할 필요없이 단순히 파이썬의 표준 라이브러리 중에서 bisect 모듈을 사용
'''
from bisect import bisect, bisect_left, bisect_right
from builtins import input

'''
# 정렬된 배열에서 특정 수의 개수 구하기
 - N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
 - 이 수열에서 x가 등장하는 횟수를 계산 
# Developer`s Kick!
 - 
 
Input01
7 2
1 1 2 2 2 2 3 3

Output01
4

Input02
7 4
1 1 2 2 2 2 3 3

Output02
-1
'''

'''
def count():
    n, x = map(int, input().split())

    data = list(map(int, input().split()))
    data.sort()

    if data.count(x) == 0:
        print(-1)
    else:
        print(data.count(x))
'''
# 정렬된 수열에서 값이 x인 원소의 개수를 세는 메소드
def count_by_value(array, x):


    # 데이터 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않은 경우
    if a is None:
        # 값이 x인 원소의 개수는 0개이므로 0 반환
        return 0

    # x가 마지막 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    # 개수 반환
    return b - a + 1

# 처음 위치를 찾는 이진탐색 메소드
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우, 인덱스 반환
    if mid == 0 or target > array[mid - 1] and array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우, 왼쪽 확인
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None

    n = len(array)

    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 오른쪽에 있는 경우, 인덱스 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid

    # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽을 확인
    elif array[mid] > target:
        return last(array, target, start, mid - 1)

    # 중간점의 값보다 찾고자 하는 값이 크거나 같은 경우, 오른쪽을 확인
    else:
        return last(array, target, mid + 1, end)

def solution():

    # 데이터 개수 N, 찾고자 하는 값 x 입력 받기
    n, x = map(int, input().split())

    # 전체 데이터 입력받기
    array = list(map(int, input().split()))

    # 값이 x인 데이터 개수 계산
    # cnt = count_by_value(array, x)
    cnt = count_by_range(array, x, x)


    # 값이 x인 원소가 존재하지 않는다면.
    if cnt == 0:
        print(-1)
    # 값이 x인 원소가 존재한다면.
    else:
        print(cnt)

'''
# 정렬된 배열에서 특정 수의 개수 구하기 - Library Version
 - N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
 - 이 수열에서 x가 등장하는 횟수를 계산 
# Developer`s Kick!
 - bisect 사용
 
Input01
7 2
1 1 2 2 2 2 3 3

Output01
4

Input02
7 4
1 1 2 2 2 2 3 3

Output02
-1
'''

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

'''
# 고정점 찾기
 - 고정점이란? 수열의 원소 중에서 그 값이 인덱스와 동일 원소를 의미
 - 고정점을 출력하는 프로그램을 작성
# Developer`s Kick!
 - 선형탐색 X
 - 이진탐색으로 해결!
 
Input01
5
-15 -6 1 3 7

Output01
3

Input02
7
-15 -4 2 8 13 15

Output02
2

Input03
7
-15 -4 8 9 13 15

Output03
-1
'''
# 이진 탐색 소스코드( 재귀 함수 )
def binary_search(array, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    # 고정점을 찾은 경우, 인덱스 반환
    if array[mid] == mid:
        return mid
    
    # 중간점이 가리키는 위치의 값보다 중간점이 작은 경우, 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)

    # 중간점이 가리키는 위치의 값보다 중간점이 큰 경우, 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)
    
def fixed_point():

    n = int(input())
    array = list(map(int, input().split()))

    # 이진탐색(binary search) 수행
    index = binary_search(array, 0, n - 1)

    # 고정점이 없는 경우, -1 출력
    if index is None:
        print(-1)

    # 고정점이 있는 경우, 해당 인덱스 출력
    else:
        print(index)

'''
# 공유기 설치
 - C개의 공유기를 N개의 집에 적당히 설치해서 가장 인접한 두 공유기 사아의 거리를 최대로 하는 프로그램 작성
# Developer`s Kick! 
 - 파라메트릭 서치 유형 문제
 - C개의 공유기보다 많은 수의 공유기 설치가 가능하다면, 가장 인접한 두 공유기 사이의 거리 값을 증가시켜서 
   더 큰 값에 대해서도 성립하는지 체크하기 위해 다시 탐색을 수행함

Input01
5 3
1
2
8
4
9

Output01
3

'''
def wifi():
    # 집의 개수(N)와 공유기 개수(C) 입력
    n, c = map(int, input().split())

    # 전체 집의 좌표 정보를 입력받기
    array = []
    for _ in range(n):
        array.append(int(input()))

    # 이진 탐색 수행을 위한 정렬 수행
    array.sort()

    # 가능한 최소 거리(min gap)
    start = 1

    # 가능한 최대 거리(max gap)
    end = array[-1] - array[0]

    ret = 0

    while (start <= end):
        # mid는 가장 인접한 두 공유기 사이의 거리(gap)를 의미
        mid = (start + end) // 2
        value = array[0]
        cnt = 1

        # 현재 mid 값을 이용해 공유기 설치
        for i in range(1, n): # 앞에서부터 차근차근 설치
            if array[i] >= value + mid:
                value = array[i]
                cnt += 1
        # C개 이상의 공유기를 설치할 수 있는 경우, 거리 증가
        if cnt >= c:
            start = mid + 1

            # 최적의 결과 저장
            ret = mid

        # C개 이상의 공유기를 설치할 수 없는 경우, 거리 감소
        else:
            end = mid - 1

    print(ret)




if __name__ == "__main__":
    # solution()
    # fixed_point()
    wifi()
