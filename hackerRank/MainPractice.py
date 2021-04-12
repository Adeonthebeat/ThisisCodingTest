

def Runner_Up():
    # Find the Runner-Up Score!
    # Given the participants ' score sheet for your University Sports Day,
    # you are required to find the runner-up score.
    # You are given  scores. Store them in a list and find the score of the runner-up.

    n = 5
    arr = [2, 3, 6, 6, 5]

    # (1)
    # max_num = max(arr)
    #
    # for i in arr:
    #     if max_num == max(arr):
    #         arr.remove(max_num)
    #     max_num = max(arr)
    # #print(max_num)
    #
    # return max_num

    # (2)
    arr.sort()
    arrList = list(set(arr))

    return arrList[-2]

def Nested_Lists(N):
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

    scored_list = []

    # find name, the second lowest grade.
    for _ in range(N):
        name = input()
        score = float(input())
        scored_list.append([name, score])

    second_score = sorted(set(score for name, score in scored_list))[1]
    second_name  = sorted(set(name for name, score in scored_list if second_score == score))

    return second_name



if __name__ == "__main__":
    # print(Runner_Up())
    print(Nested_Lists(5))