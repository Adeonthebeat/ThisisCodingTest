import sys

# 최단경로 알고리즘 : 가장 짦은 경로를 찾는 알고리즘
# 그래프를 이용해서 표현함 -> 각 지점 : 노드 | 도로: 간선
# 최단거리 알고리즘 : 다익스트라 최단경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘
# 다익스트라 최단경로 알고리즘
# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘
# 다익스트라 최단경로 알고리즘이 진행되면서, 한 단계당 하나의 노드에 대한 최단거리를 찾는 것이 핵심

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



# 간단한 다익스트라 최단경로 알고리즘
# 시간복잡도 : O(V2) | V = 노드의 개수 
# 1차원 리스트를 선언 후, 단계마다 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드를 선택하기 위해 1차원 리스트이 모든 원소를 순차탐색
def Dijkstras():
    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())    # 노드의 개수, 간선의 개수

    start = int(input())                # 시작 노드 번호를 입력받기

    graph = [[] for i in range(n + 1)]  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기

    visited = [False] * (n + 1)         # 방문한 적이 있는지 체크하는 목적의 리스트 만들기

    distance = [INF] * (n + 1)          # 최단거리 테이블을 모두 무한으로 초기화

    # 모든 간선 정보를 입력받기
    for _ in range(m):
        # a번 노드에서 b번으로 가는 비용이 c라는 의미
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    # 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드의 번호를 반환
    # n : 노드의 개수
    def get_smallest_node():
        min_value = INF
        index = 0                   # 최단거리가 가장 짧은 노드
        for i in range(1, n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    # 다익스트라
    # start : 시작점
    def dijkstras(start):
        distance[start] = 0  # 시작노드 초기화
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]

        # 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
        for i in range(n - 1):
            # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
            now = get_smallest_node()
            visited[now] = True

            # 현재노드와 연결된 다른 노드를 확인
            for j in graph[now]:
                cost = distance[now] + j[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstras(start)

    for i in range(1, n + 1):
        # 도달 할 수 없는 거리 INFINITY
        if distance[i] == INF:
            print("INFINITY")
        else:
            print(distance[i])


if __name__ == "__main__":
    Dijkstras()
