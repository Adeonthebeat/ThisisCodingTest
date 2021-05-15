import heapq
import sys
import string
import numpy
import textwrap


###########################################################
# 자동 코드 정렬 ctrl +alt + i

'''
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

def Dijkstras_HEAP():

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstras_HEAP(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:
            # 가장 최단거리가 짧은 노드 정보 꺼내기
            dist, now = heapq.heappop(q)

            # 이미 처리된 적이 있는 노드라면, 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 인접한 노드 확인
            for i in graph[now]:

                # cost 계산
                # i[0] = b의 노드 | i[1] = c의 비용
                cost = dist + i[1]

                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, HEAP에서 PUSH
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstras_HEAP(start)

    for i in range(1, n+1):
        if distance[i] == 'INF':
            print("INFINITY")
        else:
            print(distance[i])


def Dijkstras():
    input = sys.stdin.readline
    INF = int(1e9)

    # 세팅
    n, m = map(int, input().split())
    start = int(input())

    graph = [[] for i in range(n + 1)]
    visited = [False] * (n + 1)
    distance = [INF] * (n + 1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def get_smallest_node():
        min_value = INF
        index = 0
        for i in range(1, n+1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstras(start):
        distance[start] = 0
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n-1):
            now = get_smallest_node()   # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstras(start)

    for i in range(1, n+1):
        if distance[i] == "INF":
            print("INFINITY")
        else:
            print(distance[i])


def Nested_Lists(N):
    scored_list = []
    for _ in range(N):
        name = input()
        score = float(input())
        scored_list.append((name, score))

    second_score = sorted(set(score for name, score in scored_list))[1]
    second_name = sorted(set(name for name, score in scored_list if second_score == score))
    return second_name

def Choose_BowlingBall():
    n, m = map(int, input().split())

    data = list(map(int, input().split()))

    data.sort()

    arr = [0] * 11

    for i in data:
        arr[i] += 1

    ret = 0

    for i in arr:
        n -= arr[i]
        ret += arr[i] * n
    print(ret)

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    sum_value = 0
    previous = 0
    length = len(food_times)

    q = []
    for i in range(len(food_times)):
        # (음식종류, 시간)
        heapq.heappush(q, (food_times[i], i+1))

    while sum_value + (q[0][0] - previous) * length <= k:
        # 음식
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length

        length -= 1
        previous = now

    ret = sorted(q, key=lambda x: x[1])
    return ret[(k - sum_value) % length][1]


if __name__ == "__main__":
    # Dijkstras()
    # Dijkstras_HEAP()
    Choose_BowlingBall()
