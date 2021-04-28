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


if __name__ == "__main__":
    Dijkstras()
    # print(Nested_Lists(5))
