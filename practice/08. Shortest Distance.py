import heapq
import sys

# 최단경로 알고리즘 : 가장 짦은 경로를 찾는 알고리즘
# 그래프를 이용해서 표현함 -> 각 지점 : 노드 | 도로: 간선
# 최단거리 알고리즘 : 다익스트라 최단경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘
# 다익스트라 최단경로 알고리즘
# 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘
# 다익스트라 최단경로 알고리즘이 진행되면서, 한 단계당 하나의 노드에 대한 최단거리를 찾는 것이 핵심

# HEAP을 이용한 다익스트라 알고리즘
# 개선된 다익스트라 알고리즘에서는 기본적으로 힙(heap)자료구조를 이용
# 힙(Heap)자료구조를 이용하게 되면 특정노드까지의 최단 거리 정보를 힙에 담아 처리하므로 출발노드로부터 가장 거리가 짧은노드를 더욱 빠르게 찾을 수 있음
#
# HEAP이란?
# HEAP 자료구조는 우선순위(priority_queue)를 구현하기 위해 사용하는 자료구조
# 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제함
# 우선순위 큐를 구현할 때는 내부적으로 최소힙 혹은 최대힙을 이용(Default: 최소힙)
# 최소힙을 사용할 때는 값이 가장 낮은 데이터가 먼저 삭제
# 최대힙은 값이 큰 데이터가 가장 먼저 삭제
# 최대 힙(max_heap)으로 사용하고 싶다면, 값에 음수 부호(-)를 붙여서 넣었다가
# heapq.heappop 할 때 다시 음수 부호(-)를 붙여 원래의 값으로 돌리면 된다.

# 스택(stack): 가장 나중에 삽입된 데이터를 추출
# 큐(queue)  : 가장 먼저 삽입된 데이터를 추출
# 우선순위 큐(priority_queue): 가장 우선순위가 높은 데이터를 추출

# 다익스트라(HEAP)
# 사용시기 : 한지점에서 다른 특정지점까지 최단경로를 구하는 경우
# 핵심원리 : 방문하지 않은 노드 중 최단거리를 갖는 노드를 찾음
# 리스트 - 1차원
# 분류 : 그리디(Greedy)
# 시간복잡도 : O(ElogV)

# 플로이드워셜
# 사용시기 : 모든 지점에서 다른 모든 지점까지의 최단경로를 구하는 경우
# 핵심원리 : 방문하지 않는 노드 중 최단거리를 갖는 노드를 찾지 않음
# 리스트 - 2차원
# 분류 : 다이나믹프로그래밍(DP)
# 시간복잡도 : O(N^3)
# Dab = Distance A to B
# 점화식 : Dab = min(Dab, Dak + Dkb)

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

def Dijkstras_heap():

    input = sys.stdin.readline
    INF = int(1e9)

    n, m = map(int, input().split())    # 노드의 개수, 간선의 개수
    start = int(input())                # 시작 노드 번호를 입력받기
    graph = [[] for i in range(n+1)]    # 각 노드에 연결되어 있는 노드정보를 담는 리스트 만들기
    distance = [INF] * (n+1)            # 최단거리 테이블을 모두 무한으로 초기화

    # 모든 간선 정보 세팅
    for _ in range(m):# 간선의 개수 만큼
        a, b, c = map(int,input().split())
        # a번 노드에서 b의 노드로 가는 c의 비용
        graph[a].append((b, c))

    def dijkstras_heap(start):
        q = []

        # 시작노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        # 큐가 비어있지 않다면.
        while q:
            # 가장 최단거리가 짧은 노드 정보 꺼내기
            # now : Node
            dist, now = heapq.heappop(q)

            # 이미 처리된 적이 있는 노드라면, 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 인접한 노드 확인
            for i in graph[now]:
                # i[0] = b의 노드 | i[1] = c의 비용
                cost = dist + i[1]

                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, HEAP에서 POP
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstras_heap(start)

    for i in range(1, n+1):
        if distance[i] == 'INF':
            print("INFINITY")
        else:
            print(distance[i])
'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''
# 플로이드워셜 알고리즘
def Floyd_Warshall():

    # 무한 값 세팅
    INF = int(1e9)

    # 노드의 개수와 간선의 개수 세팅
    n = int(input())
    m = int(input())

    # 2차원리스트(그래프)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n+1):
        for b in range(1, n+1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아 그 값으로 초기화
    for _ in range(m):
        # A에서 B로 가는 비용은 C라고 설정
        a, b, c = map(int, input().split())
        graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                # min(a -> b, a -> x -> b)
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    # 수행된 결과 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
            if graph[a][b] == 1e9:
                print("INFINITY", end=" ")
            # 도달할 수 있는 경우 거리를 출력
            else:
                print(graph[a][b], end=" ")
        print()

'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

4 2
1 3
2 4
3 4
'''
# 문제요약 : 1번회사에서 출발해 X를 거쳐 K로 가는 최단거리를 구하라.
def future_city():

    INF = int(1e9)

    # 노드, 간선의 개수 체크
    n, m = map(int, input().split())
    # 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선에 대한 정보를 입력받아 그 값으로 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        # 서로에게 가는 비용은 1 * 주의
        graph[a][b] = 1
        graph[b][a] = 1

    # 거쳐갈 노드 X와 최종 목적지 노드 K 입력
    x, k = map(int, input().split())

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    distance = graph[1][k] + graph[k][x]

    if distance >= INF:
        print("-1")
    else:
        print(distance)


'''
3 2 1
1 2 4
1 3 2
'''
# 전보문제
# 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇개이며,
# 도시들이 모두 메시지를 받는데까지 걸린 시간은 얼마인지 계산하시오.
def telegram():

    INF = int(1e9)
    input = sys.stdin.readline

    n, m, start = map(int, input().split())

    graph = [[] for i in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    def dijkstras(start):
        q = []
        # 시작노드로 가기 위한 최단경로는 0으로 설정하여 큐에 삽입
        heapq.heappush(q, (0, start))
        distance[start] = 0

        # 큐가 비어있지 않다면.
        while q:
            dist, now = heapq.heappop(q)
            # 이미 처리된 적이 있는 노드라면, 무시
            if distance[now] < dist:
                continue

            # 현재 노드와 연결된 인접한 노드 확인
            for i in graph[now]:
                # i[0] = b의 노드 | i[1] = c의 비용
                cost = dist + i[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우, HEAP에서 POP
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstras(start)

    # 도달할 수 있는 노드 개수
    cnt = 0

    # 도달할 수 있는 노드 중 가장 멀리 있는 노드의 거리
    max_distance = 0

    for d in distance:
        # 도달할 수 있는 노드인 경우
        if d != INF:
            cnt += 1
            max_distance = max(max_distance, d)

    print(cnt-1, max_distance)







    return ""

if __name__ == "__main__":
    # Dijkstras()
    # Dijkstras_heap()
    # Floyd_Warshall()
    # future_city()
    telegram()