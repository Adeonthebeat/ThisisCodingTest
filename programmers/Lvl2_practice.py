'''

'''

'''
# 최댓값과 최솟값
'''
def Max_min(s):
    answer = ""

    num_list = list(map(int, s.split(' ')))

    max_num = max(num_list)
    min_num = min(num_list)

    answer = str(min_num) +" "+ str(max_num)
    print(answer)

if __name__ == "__main__":
    Max_min("1 2 3 4")
