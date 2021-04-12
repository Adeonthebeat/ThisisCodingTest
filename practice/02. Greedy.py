
# Greedy Algorithms
# 거스름돈의 최소 개수 - greedy_coin


def greedy_coin(n):
    coin_types = [500, 100, 50, 10]

    cnt = 0
    for coin in coin_types:
        cnt += n//coin  # (1) 카운트 += 1260//500 = 몫
        n %= coin       # (1) 1260/500 = 260
    return cnt

def greedy_max_sum():
    # point = 가장 큰 수를 연속적으로 더해주고, 두 번째로 큰수를 사이사이 넣어서 계산 = 최대값
    # 가장 큰 수가 더해주는 횟수 계산이 중요!

    # n, m, k = map(int, input().split())
    # n = 배열의 수
    # m = 최대로 더할 수 있는 수
    # k = 연속으로 더할 수 있는 수
    # data = list(map(int, input().split()))
    
    n, m, k = 5, 8, 3
    data = [2, 4, 5, 4, 6]
    
    data.sort()
    first = data[n-1]
    second = data[n - 2]
    cnt = (m//(k+1)) * k    # (최대로 더할 수 있는 수 // 연속으로 더할 수 있는 수 + 1) * 연속으로 더할 수 있는 수
    cnt += m % (k+1)        # 나머지 = 최대로 더할 수 있는 수의 나머지

    ret = 0
    # ret += first * cnt
    # ret += second * (m - cnt)
    ret = (first * cnt) + (second * (m - cnt))

    return ret

def number_card_game():
    # point = 각 행마다 가장 작은 수를 찾은 뒤 그 수 중 가장 큰수를 찾는 방법!

    # 3 3
    # 3 1 2
    # 4 1 4
    # 2 2 2

    n, m = map(int, input().split())

    # 1) ret = []
    ret = 0
    for i in range(n):
        data = list(map(int, input().split()))

        # 2) min_value = min(data)
        min_value = min(data)
        # 3)
        # min_value = 10001
        # for a in data:
        #     min_value = min(a, min_value)

        # 1) ret.append(min_value)
        ret = max(ret, min_value)

    return ret

def to_one():

    # N을 1로 만드는 문제이며, N을 나누거나 -1을 하면서 1을 만들어야함
    # point = N을 최대한 많이 나누기를 하는 것.

    # N, k = map(int, input().split()) # 25 3
    N, k = 25, 3
    cnt = 0
    ret = 0
    while True:
        # Point - Minus
        target = (N // k) * k
        ret += (N - target)     # += 주의

        N = target              # 주의!

        if N < k:
            break

        # Point - Divide
        N //= k
        ret += 1


    # Point - Minus
    ret += N - 1                # 마지막으로 남은 수에 -1

    return ret

if __name__ == "__main__":
    # print(greedy_coin(1260))
    # print(greedy_max_sum())
    # print(number_card_game())
    # print(to_one())
    print('############################')
    print('######### Greedy ###########')
    print('############################')

