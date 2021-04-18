# 정렬(Sorting) : 데이터를 특정한 기준에 따라서 순서대로 나열하는 것
# 종류 : 선택정렬, 삽입정렬, 퀵정렬, 계수정렬 등

# 선택정렬 : 가장 작은 것을 선택하는 가장 원시적인 알고리즘
# 가장 작은 데이터를 선택에 맨 앞에 있는 데이터와 바꾸고,
# 그 다음 작은 데이터를 선택해 앞에서 두 번쨰 데이토와 바꾸는 과정을 반복
# 시간복잡도 : O(n2)

# 삽입정렬 : 특정한 데이터를 적절한 위치에 삽입하는 알고리즘
# 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입
# 정렬이 거의 되어있는 상황에서 강력한 알고리즘이며
# 첫번째 데이터는 정렬이 되어있다는 가정 하에 두번째 데이터부터 시작
# 시간복잡도 : O(n2)

# 퀵정렬 : 기준을 설정한 후, 큰 수와 작은 수를 교환 및 리스트를 반으로 나누는 알고리즘
# 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 교환방식
# 기준 = 피벗
# 분할방식 : 호어방식
# 시간복잡도 : O(NlogN) - 최악(O(N^2))

# 계수정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만, 매우 빠른 정렬 알고리즘
# 계수정렬은 각 위치를 만들어 넣고, 그 위치에 각 데이터를 넣어서 보여줌
# 데이터의 크기가 한정되어 있고 데이터의 크기가 중복되어 있을 때 쓰면 좋다
# 시간복잡도 : O(N+K)

def select_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def swap_pratice():
    array = [3, 5]

    # swap
    array[0], array[1] = array[1], array[0]

    return array


def insert_sort():
    array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

    for i in range(len(array)):
        # 인덱스 i부터 1씩 감소
        for j in range(i, 0, -1):
            # j에서 j - 1이랑 비교
            if array[j] < array[j - 1]:
                # swap
                array[j], array[j - 1] = array[j - 1], array[j]
            # 자기 자신보다 작은 데이터면, break
            else:
                break

    return array


def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start  # 첫 번째 데이터가 피벗(기준)
    left = start + 1
    right = end

    while left <= right:

        # 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸다면, 피벗과 작은 데이터 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면, 작은 데이터와 큰 데이터 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 분할 이후, 왼쪽과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    return array


def quick_sort_list_comprehension(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    # 분할된 왼쪽
    left_side = [x for x in tail if x <= pivot]

    # 분할된 오른쪽
    right_side = [x for x in tail if x > pivot]

    return quick_sort_list_comprehension(left_side) + [pivot] + quick_sort_list_comprehension(right_side)


# [ 이것이 코딩테스트다 ] 18일차 by abcd8637
def quick_sort_append(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left_side, right_side = list(), list()

    for i in range(1, len(array)):
        if array[i] < pivot:
            left_side.append(array[i])
        else:
            right_side.append(array[i])

    return quick_sort_append(left_side) + [pivot] + quick_sort_append(right_side)

# 계수정렬
def count_sort(array):
    # 모든 범위를 포함하는 리스트 선언(+1) -> 0으로 초기화
    cnt = [0] * (max(array) + 1)

    # 각 데이터에 해당하는 인덱스의 값 증가
    for i in range(len(array)):
        cnt[array[i]] += 1

    # 리스트에 기록된 정렬 정보 확인
    for i in range(len(cnt)):
        for j in range(cnt[i]):
            print(i, end=' ')  # 띄어쓰기 구분으로 등장한 횟수만큼 인덱스 출력

    return ""


def sorted_practice(array):
    # sorted
    ret = sorted(array)
    print("### sorted ::: ", ret)

    # sort
    arr = array
    arr.sort()
    print("### sort   ::: ", arr)

    return ""


# key를 매개변수로 입력받는 sorted
def key_sort_practice(arr):
    ret = sorted(arr, key=setting)
    return ret


def setting(data):
    return data[1]


#########################################################################
# 위에서 아래로
# 단순접근 -> 라이브러리로 해결
def up_to_down():
    N = int(input())

    list = []
    for i in range(N):
        list.append(int(input()))

    arr = sorted(list, reverse=True)

    for i in arr:
        print(i, end=' ')

    return ""


# 성적 낮은 순으로 출력
def low_grade():
    N = int(input())

    list = []
    for i in range(N):
        name, scores = input().split()
        list.append((name, int(scores)))                    # 개발자의 킥1

    array = sorted(list, key=lambda student: student[1])    # 개발자의 킥2

    for student in array:
        print(student[0])

    return ""

# 두 배열의 원소 교체
# a 배열의 가장 작은 수를 b 배열의 가장 큰 수와 교체하여 a배열의 합이 제일 크게 만드는 것
def two_array_change():

    # n, m = map(int, input().split())
    n, k = 5, 3
    # a = list(map(int, input().split()))
    # b = list(map(int, input().split()))
    a = [1, 2, 5, 4, 3]
    b = [5, 5, 6, 6, 5]

    # a는 오르차순 b는 내림차순으로 해서 서로 비교
    a.sort()
    b.sort(reverse=True)

    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    return sum(a)

if __name__ == "__main__":
    # array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
    # array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
    # arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

    # print(select_sort())
    # print(swap_pratice())
    # print(insert_sort())
    # print(quick_sort(array, 0, len(array) - 1))
    # print(quick_sort_list_comprehension(array))
    # print(quick_sort_append(array))
    # print(count_sort(array))
    # print(sorted_practice(array))
    # print(key_sort_practice(arr))
    # print(up_to_down())
    # print(low_grade())
    print(two_array_change())
