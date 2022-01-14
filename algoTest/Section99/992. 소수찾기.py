from itertools import permutations


# "17"	3
# "011"	2

def check(n):
    if int(n) < 2:
        return False
    for i in range(2, n // 2 + 1):
        if int(n) % i == 0:
            return False
    return True


def solution(numbers):
    answer = []
    cnt = 0
    for i in range(1, len(numbers) + 1):
        temp = list(map(''.join, permutations(list(numbers), i)))
        for j in list(set(temp)):
            if check(int(j)):
                answer.append(int(j))

    print(len(list(set(answer))))


if __name__ == "__main__":
    solution("17")
    solution("011")
