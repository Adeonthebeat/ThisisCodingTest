# 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
# 오버플로: 데이터가 넘쳐흐를 때, 발생함
# 언더플로: 데이터가 없을 때, 삭제연산을 수행하면 발생함


from collections import deque


# 스택 : 선입후출 구조 및 후입선입 구조
def stack_practice():
    stack = []

    # 삽입 5, 2, 3, 7, 삭제, 삽입 1, 4, 삭제
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    print("### stack        ::: ", stack)  # 최하단 원소부터 출력
    print("### stack[::-1]  ::: ", stack[::-1])  # 최상단 원소부터 출력

    return stack


# 큐 : 선입선출 구조
def queue_practice():
    # deque는 스택과 큐의 장점을 모두 채택.
    # deque는 속도가 리스트 자료형에 비해 효율적이며, queue 라이브러리를 이용하는 것보다 간단함

    queue = deque()

    # 삽입 5, 2, 3, 7, 삭제, 삽입 1, 4, 삭제
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print("### queue        ::: ", queue)  # 선입한 원소부터 출력
    queue.reverse()
    print("### queue        ::: ", queue)  # 후입한 원소부터 출력

    return queue


# 재귀함수 : 자기 자신을 다시 호출하는 함수
def recursive_function():
    print("재귀함수 호출")
    recursive_function()


# 재귀함수 : 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 100:
        return

    print(i, '번째 재귀함수에서 ', (i + 1), ' 번째 함수 호출를 종료')
    return recursive_function(i + 1)


# for문
def factorial_iterative(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i

    return ret


# 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n - 1)
    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    # print(stack_practice())
    # print(queue_practice())
    # print(recursive_function(1))
    print(factorial_iterative(100))
    print(factorial_recursive(100))
