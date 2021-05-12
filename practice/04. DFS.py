
from collections import deque
'''
# 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
# 오버플로: 데이터가 넘쳐흐를 때, 발생함
# 언더플로: 데이터가 없을 때, 삭제연산을 수행하면 발생함

# DFS(Deep First Search) : 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# 그래프 => 노드(Node) = 정점(Vertex) | 간선(Edge)로 구분
# 인접행렬(Adjacency Matrix): 2차원 배열로 그래프의 연결관계를 표현하는 방식 = 2차원 배열에 각 노드가 연결된 형태로 기록하는 방식
# 인접리스트(Adjacency List): 리스트로 그래프의 연결관계를 표현하는 방식
# 인접행렬과 인접리스트 차이점
# 1) 인접행렬은 노드 개수가 많을수록 메모리를 불필요하게 낭비. 반면, 인접리스트는 효율적으로 사용
# 2) 인접리스트는 두 노드가 연결되어 있는지 얻는 정보가 느리다. 인접리스트는 데이터를 하나하나 확인하기 때문이다.
'''

# 스택 : 선입후출 구조 및 후입선입 구조
def stack_practice():
    stack = []

    # 삽입 5, 2, 3, 7, 삭제, 삽입 1, 4, 삭제
    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.append(4)
    stack.pop()

    print("### stack        ::: ", stack)  # 최하단 원소부터 출력
    print("### stack[::-1]  ::: ", stack[::-1])  # 최상단 원소부터 출력

    return stack


# 큐 : 선입선출 구조
def queue_practice():
    # deque는 스택과 큐의 장점을 모두 채택.
    # deque는 속도가 리스트 자료형에 비해 효율적이며, queue 라이브러리를 이용하는 것보다 간단함

    queue = deque()

    # 삽입 5, 2, 3, 7, 삭제, 삽입 1, 4, 삭제
    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.append(4)
    queue.popleft()

    print("### queue        ::: ", queue)  # 선입한 원소부터 출력
    queue.reverse()
    print("### queue        ::: ", queue)  # 후입한 원소부터 출력

    return queue


# 재귀함수 : 자기 자신을 다시 호출하는 함수
def recursive_function():
    print("재귀함수 호출")
    recursive_function()


# 재귀함수 : 자기 자신을 다시 호출하는 함수
def recursive_function(i):
    if i == 100:
        return

    print(i, '번째 재귀함수에서 ', (i + 1), ' 번째 함수 호출를 종료')
    return recursive_function(i + 1)


# for문
def factorial_iterative(n):
    ret = 1
    for i in range(1, n + 1):
        ret *= i

    return ret


# 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n - 1)
    return n * factorial_recursive(n - 1)

def Adjacency_Matrix():
    INF = 999999999
    graph = [
        [0, 7, 5],
        [7, 0, INF],
        [5, INF, 0]
    ]
    return graph


# 인접리스트
def Adjacency_List():
    # Row가 3개인 2차원 리스트로 인접리스트 표현
    graph = [[] for _ in range(3)]

    # Node 0에 연결된 노드정보 저장 (노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    # Node 1에 연결된 노드정보 저장 (노드, 거리)
    graph[1].append((0, 7))

    # Node 2에 연결된 노드정보 저장 (노드, 거리)
    graph[2].append((0, 5))

    return graph


# DFS(Depth First Search) : 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# DFS 동작 원리 : 스택
# DFS 구현 방법 : 재귀함수 이용
def dfs(graph, v, visited):
    visited[v] = True  # 현재 노드를 방문 처리
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    return ""


# BFS(Breadth First Search) : 너비 우선 탐색이라고 하며, 가까운 노드부터 탐색하는 알고리즘
# BFS 동작 원리 : 큐
# BFS 구현 방법 : 큐자료구조
def bfs(graph, start, visited):
    queue = deque([start])  # deque 라이브러리를 통한 큐

    # 현재노드에 방문처리
    visited[start] = True

    # 큐가 빈 값일 때까지 반복
    while queue:

        # 큐에서 하나의 원소를 출력
        v = queue.popleft()
        print(v, end=' ')

        # 해당 원소의 연결된 아직 방문하지 않은 원소를 큐에 삽입.
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

    return ""


# N, M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오
def freeze_beverage():
    # n, m = map(int, input().split())
    n, m = 15, 14

    # input = [
    #     00000111100000
    #     11111101111110
    #     11011101101110
    #     11011101100000
    #     11011111111111
    #     11011111111100
    #     11000000011111
    #     01111111111111
    #     00000000011111
    #     01111111111000
    #     00011111111000
    #     00000001111000
    #     11111111110011
    #     11100011111111
    #     11100011111111
    # ]

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))  # split 아님

    def dfs_fb(x, y):
        if x < 0 or x >= n or y < 0 or y >= m:
            return False

        if graph[x][y] == 0:
            graph[x][y] = 1
            dfs_fb(x - 1, y)  # 상
            dfs_fb(x + 1, y)  # 하
            dfs_fb(x, y - 1)  # 좌
            dfs_fb(x, y + 1)  # 우
            return True

        return False

    ret = 0
    for i in range(n):
        for j in range(m):
            if dfs_fb(i, j) == True:
                ret += 1

    return ret


# 현재 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
# 이때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어 있다.
# 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이때 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
# 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.
def maze_runner():
    # input = [
    # 5 6
    # 101010
    # 111111
    # 000001
    # 111111
    # 111111
    # ]

    # 세팅
    N, M = map(int, input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input())))

    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs_mr(x, y):
        queue = deque()
        queue.append((x, y))

        # 큐가 빌 때까지
        while queue:
            x, y = queue.popleft()  # 중요!
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 미로찾기 공간 범위 벗어난 경우, 무시
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    continue

                # 괴물!!
                if graph[nx][ny] == 0:
                    continue

                # 초기값은 1.
                # 다음 노드가 처음 방문 한 경우, 현재 노드보다 거리가 한 칸 더 멀다
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))
        return graph[N - 1][M - 1]

    return bfs_mr(0, 0)


if __name__ == "__main__":

    # print(stack_practice())
    # print(queue_practice())
    # print(recursive_function(1))
    # print(factorial_iterative(100))
    # print(factorial_recursive(100))

    # print(Adjacency_Matrix())
    # print(Adjacency_List())

    ########################################################
    # graph = [
    #     [],
    #     [2, 3, 8],
    #     [1, 7],
    #     [1, 4, 5],
    #     [3, 5],
    #     [3, 4],
    #     [7],
    #     [2, 6, 8],
    #     [1, 7]
    # ]
    # visited = [False] * 9

    # print(dfs(graph, 1, visited))
    # print(bfs(graph, 1, visited))
    ########################################################

    # print(freeze_beverage())
    print(maze_runner())
