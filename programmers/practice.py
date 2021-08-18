'''
프로그래머스 1단계 풀이
- 최대공약수와 최소공배수
- 문자열 내 마음대로 정렬하기
- 모의고사(완전탐색)
'''

from math import gcd
import itertools

'''
# 최대공약수와 최소공배수
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

n	m	return
3	12	[3, 12]
2	5	[1, 10]
'''


def solution(n, m):
    answer = []

    a = gcd(n, m)
    b = (n * m) // a

    answer = [a, b]

    return answer


'''
# 문자열 내 마음대로 정렬하기
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 
각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

strings	n	return
["sun", "bed", "car"]	1	["car", "bed", "sun"]
["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]

'''


def solution(strings, n):
    # sort를 Strings의 각 객체의 n번째 글자기준으로 하면서 각 객체의 순서를 따름 
    answer = sorted(strings, key=lambda x: (x[n], x))
    return answer


'''
# 모의고사 문제
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

answers	    |   return
[1,2,3,4,5]	|   [1]
[1,3,2,4,2]	|   [1,2,3]
'''


def pre_test(answers):
    answer = []

    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    c1, c2, c3 = 0, 0, 0

    for i in range(len(answers)):
        if answers[i] == a1[i % len(a1)]:
            c1 += 1
        if answers[i] == a2[i % len(a2)]:
            c2 += 1
        if answers[i] == a3[i % len(a3)]:
            c3 += 1

    temp = [c1, c2, c3]

    for number, scores in enumerate(temp):
        if scores == max(temp):
            answer.append(number + 1)

    return answer


'''
# [삼각 달팽이] 문제
정수 n이 매개변수로 주어집니다. 다음 그림과 같이 밑변의 길이와 높이가 n인 삼각형에서 맨 위 꼭짓점부터 반시계 방향으로 달팽이 채우기를 진행한 후, 
첫 행부터 마지막 행까지 모두 순서대로 합친 새로운 배열을 return 하도록 solution 함수를 완성해주세요.

입출력 예
n	result
4	[1,2,9,3,10,8,4,5,6,7]
5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
6	[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]

Level 1부터 잘하자....
'''


def snail(n):
    array = [[0 for x in range(y)] for y in range(1, n + 1)]
    num = 1
    x = -1
    y = 0
    test = n % 3

    for i in range(n, 0, -1):
        for j in range(i):
            if n % 3 == test:
                x = x + 1
            elif n % 3 == (test - 1) or n % 3 == (test + 2):
                y += 1
            else:
                x -= 1
                y -= 1
            array[x][y] = num
            num += 1

        n = n - 1
    print("##########################")
    print(list(itertools.chain(*array)))
    print("##########################")

    return list(itertools.chain(*array))


'''
유용한 getMax 함수
'''


def getMax(n):
    answer = 0

    if n == 1:
        answer = 1
    else:
        answer = getMax(n - 1) + n

    return answer


'''
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 
숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 
소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

'''


def sosu(nums):
    cnt = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if isPrimeNums(nums[i], nums[j], nums[k]):
                    cnt += 1
    return cnt


def prime(nums):
    cnt = 0
    num_list = list(itertools.combinations(nums, 3))
    for i in num_list:
        if isPrimeNums(i[0], i[1], i[2]): cnt += 1
    return cnt


'''
# 소수 판별
'''


def isPrimeNums(a, b, c):
    tot = a + b + c
    for i in range(2, tot):
        if tot % i == 0:
            return False
    return True


'''
배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, 
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 
나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.
'''


def k_number(array, commands):
    for i in range(len(commands)):
        temp = array[commands[i][0] - 1:commands[i][1]]

        temp.sort()

        answer = temp[commands[i][2] - 1]

    return answer


'''
점심시간에 도둑이 들어, 일부 학생이 체육복을 도난당했습니다. 다행히 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주려 합니다. 
학생들의 번호는 체격 순으로 매겨져 있어, 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있습니다. 
예를 들어, 4번 학생은 3번 학생이나 5번 학생에게만 체육복을 빌려줄 수 있습니다. 체육복이 없으면 수업을 들을 수 없기 때문에 
체육복을 적절히 빌려 최대한 많은 학생이 체육수업을 들어야 합니다.

전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 
여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 
체육수업을 들을 수 있는 학생의 최댓값을 return 하도록 solution 함수를 작성해주세요.
'''


def gym_suit(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)

    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    return n - len(set_lost)


'''
# 행렬의 덧셈
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
arr1	        arr2	        return
[[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
[[1],[2]]	    [[3],[4]]	    [[4],[6]]
'''


def sum_matrix(arr1, arr2):
    answer = []
    # for i in range(len(arr1)):
    #     arr_sum = []
    #     for j in range(len(arr2[0])):
    #         arr_sum.append(arr1[i][j] + arr2[i][j])
    #     answer.append(arr_sum)

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return arr1

def remove_min(arr):

    if(len(arr) > 1):
        list = set(arr)

        list.remove(min(list))

        arr.remove(min(arr))

        # print(list)
        print(arr)
    else:
        arr.remove(max(arr))
        arr.append(-1)
        print(arr)
    # return [i for i in arr if i > min(arr)]

def collatz(num):
    cnt = 0
    #
    # while True:
    #     if cnt == 500:
    #         break
    #     if num == 1:
    #         break
    #     if num % 2 == 0:
    #         num = num / 2
    #         cnt += 1
    #     else:
    #         num = (num * 3) + 1
    #         cnt += 1
    #
    # print(cnt if cnt != 500 else -1)

    answer = 0

    if num == 1:
        return answer

    while True:
        num = num/2 if num % 2 == 0 else (num * 3) + 1
        answer += 1
        if num == 1:
            return answer
        elif answer == 500:
            return -1
    return answer

    # for i in range(500):
    #     num = num / 2 if num % 2 == 0 else num*3 + 1
    #     if num == 1:
    #         return i + 1
    # return -1




if __name__ == "__main__":
    # print(solution(2, 5))
    # print(solution(["abce", "abcd", "cdx"], 2))
    # print(pre_test([1, 2, 3, 4, 5]))
    # print(pre_test([1, 3, 2, 4, 2]))
    # print(getMax(4))
    # snail(4)
    # print(sosu([1,2,3,4]))
    # print(prime([1,2,3,4]))
    # print(prime([1, 2, 7, 6, 4]))
    # k_number([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    # print(gym_suit(5, [2, 4], [1, 3, 5]))
    # print(gym_suit(5, [2, 4], [3]))
    # print(gym_suit(3, [3], [1]))
    # print(sum_matrix([[1,2],[2,3]], [[3,4],[5,6]]))
    # remove_min([10])
    print(collatz(8))