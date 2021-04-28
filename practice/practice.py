import sys
import string
import numpy
import textwrap

###########################################################
# 자동 코드 정렬 ctrl +alt + i

def Dijkstras():

    # 세팅
    n, m = 1,2


    def get_smallest_distnace(start):
        index = 0
        return index

    def dijkstras(start):
        return ""

def Nested_Lists(N):

    scored_list = []
    for _ in range(N):
        name = input()
        score = float(input())
        scored_list.append((name, score))

    second_score = sorted(set(score for name, score in scored_list))[1]
    second_name  = sorted(set(name for name, score in scored_list if second_score == score))
    return second_name


if __name__ == "__main__":
    # Dijkstras()
    print(Nested_Lists(5))