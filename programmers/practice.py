'''
프로그래머스 1단계 풀이
'''
import math
import re
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
# s
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 
각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

    strings	            n	return
["sun", "bed", "car"  ]	1	["car", "bed", "sun"]
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
    if (len(arr) > 1):
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
        num = num / 2 if num % 2 == 0 else (num * 3) + 1
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


'''
# 정수 제곱근 판별 문제
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

입출력
n	    return
121	    144
3	    -1
'''


def square_root(n):
    # sqrt_num = int(math.sqrt(n))
    # answer = int(math.pow(sqrt_num+1, 2))

    # sqrt_num = n ** (1/2)
    #
    # if sqrt_num % 1 == 0:
    #     print(int((sqrt_num + 1) ** 2))
    # else:
    #     print(-1)

    print(int(pow(math.sqrt(n) + 1, 2)) if math.sqrt(n) % 1 == 0 else -1)


'''
# 정수 내림차순으로 배치하기 문제
함수 solution은 정수 n을 매개변수로 입력받습니다. 
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 
예를 들어 n이 118372면 873211을 리턴하면 됩니다.

n	    return
118372	873211
'''


def num_desc(n):
    data = sorted(list(map(int, str(n))), reverse=True)

    print("".join(map(str, data)))


'''
# 하샤드 수 문제
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

입출력
arr	    return
10	    true
12	    true
11	    false
13	    false
'''


def harshad(arr):
    data = list(map(int, str(arr)))

    print(True if arr % sum(data) == 0 else False)


'''
# 핸드폰 번호 가리기 문제
프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 
전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

phone_number	return
"01033334444"	"*******4444"
"027778888"	    "*****8888"
'''


def phone_number(phone_num):
    # data = list(map(int, str(phone_num)))

    # for i in range(len(phone_num)-4):
    #     data[i] = "*"
    #
    # print("".join(map(str, data)))

    print(str("*" * (len(phone_num) - 4)) + str(phone_num[-4:]))


'''
# 자연수 뒤집어 배열로 만들기 문제
'''


def reversed_str():
    n = 12345

    rvs_str = str(n)[::-1]

    data = list(map(int, list(rvs_str)))

    print(data)

    print(list(map(int, reversed(str(n)))))


'''
# x만큼 간격이 있는 n개의 숫자 문제
- 곱셈....
'''


def practice():
    x = 2
    n = 5

    answer = []

    for i in range(1, n + 1):
        answer.append(i * x)

    print(answer)
    print([i * x + x for i in range(n)])


'''
# 직사각형 별찍기 문제
'''


def practice2():
    a, b = 5, 3

    print(('*' * a + '\n') * b)
    # for i in range(1, b+1):
    #     print("*" * a)


def sum_test():
    a, b = 3, 3
    c = 0
    answer = 0
    if a != b:
        c = a
        answer = a + b + c
    else:
        answer = a

    print(answer)


'''
# 문자열을 정수로 바꾸기
'''


def text_to_num():
    n = "-1234"
    print(int(n))
    # sum = ""
    # for i in n:
    #     sum += i
    # print(int(sum))


'''
# 문자열 내림차순으로 배치하기
'''


def desc_text():
    s = "Zbcdefg"
    re_str = str(s)[::-1]

    # print(''.join(sorted(s)[::-1]))
    print("".join(reversed(sorted(s))))


'''
# 두 정수 사이의 합
range 함수 : 연속된 숫자(정수)를 만들어주는 함수
'''


def num_sum():
    a, b = 5, 3
    print(sum(range(min(a, b), max(a, b) + 1)))


'''
# 에라토스 테네스의 체 방식
# 소수판별법 
'''


def eratones(n):
    nums = [True] * (n + 1)

    for i in range(2, len(nums) // 2 + 1):
        if nums[i]:
            for j in range(i + i, n + 1, i):
                nums[j] = False
    # print(len([i for i in range(2, n + 1) if nums[i]]))
    print(len([i for i in range(2, n + 1) if nums[i]]))


def eratonesTwo(n):
    num = set(range(2, n + 1))

    for i in range(2, n + 1):
        if i in num:
            num -= set(range(2 * i, n + 1, i))
    print(len(num))


'''
# 약수의 합
n	return
12	28
5	6
'''


def yaksu(n):
    sum = 0
    for i in range(1, n + 1):
        if n % i == 0:
            sum += i

    print(sum)


'''
# 약수의 개수와 덧셈
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

left	right	result
13	    17	    43
24	    27	    52

'''


def yaksu_cnt_plus():
    left = 13
    right = 17

    sum = 0
    for k in range(left, right + 1):
        cnt = 0
        for i in range(1, k + 1):
            if k % i == 0:
                cnt += 1
        if cnt % 2 == 0:
            sum += k
        else:
            sum -= k

    print(sum)
    # print(sum)
    # print(13 + 14 + 15 - 16 + 17 )


'''
# 나누어 떨어지는 숫자 배열
'''


def divisor():
    arr = [5, 9, 7, 10]
    div = 5

    # answer = []
    #
    # for i in arr:
    #     if i % div == 0:
    #         answer.append(i)
    # if len(answer) == 0:
    #     answer.append(-1)
    #
    # print(sorted(answer))
    print(sorted([n for n in arr if n % div == 0]) or [-1])


'''
# 자릿수 더하기 문제
'''


def number_of_sum():
    n = 123

    arr = list(map(int, str(n)))

    return sum([i for i in arr])


'''
# 문자열 다루기 기본
'''


def isTrue():
    s = "a234"
    answer = False

    re_s = re.sub('[0-9]', '', s)

    if re_s == '':
        if len(s) in range(4, 6):
            answer = True
        else:
            answer = False


'''
# 이상한 문자 만들기
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 
각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
- 제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.

'''


def weird_text():
    s = "try hello world"
    words_list = s.split()
    new_list = []

    for word in words_list:
        new_word = ""
        for i in range(len(word)):
            # new_word += word[i].upper() if i % 2 == 0 else word[i].lower()
            if i % 2 == 0:
                new_word += word[i].upper()
            elif i % 2 == 1:
                new_word += word[i].lower()

        new_list.append(new_word)
    print(" ".join(new_list))
    print(" ".join(["".join([w.upper() if i%2==0 else w.lower() for i, w in enumerate(word)]) for word in s.split()]))





'''
# 같은 수는 싫어 문제
- 같은 연속적인 수는 제거하는 문제
->> 같은 수가 아니라면, 다른 리스트에 넣으면 됨
'''


def sequetial_num_rm():
    answer = []
    arrList = [1, 1, 3, 3, 0, 1, 1]
    answer.append(arrList[0])
    for i in range(1, len(arrList)):
        if arrList[i] != arrList[i - 1]:
            answer.append(arrList[i])
    print(answer)


'''
# 같은 수는 싫어 문제
- 맨끝에 수 != 주어진 리스트의 수라면, insert.
- 미친 코드!
'''


def sequetial_num_rm2():
    answer = []
    s = [1, 1, 3, 3, 0, 1, 1]

    for i in s:
        if answer[-1:] == [i]: continue
        answer.append(i)
    print(answer)


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
    # print(collatz(8))
    # square_root(3)
    # num_desc(118372)
    # harshad(10)
    # phone_number("01033334444")
    # reversed_str()
    # practice()
    # practice2()
    # sum_test()
    # text_to_num()
    # desc_text()
    # num_sum()
    # eratones(10)
    # eratonesTwo(10)
    # yaksu(12)
    # yaksu_cnt_plus()
    # divisor()
    # number_of_sum()
    weird_text()
    # sequetial_num_rm()
    # sequetial_num_rm2()
