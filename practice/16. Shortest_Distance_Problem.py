'''
# 최단 경로 문제
- 최단 경로 알고리즘 : 그래프 상 가장 짧은 경로를 찾는 알고리즘
    - 다익스트라 알고리즘: 한 지점에서 다른 모든 지점까지의 최단 경로를 계산
    - 플로이드 워셜: 모든 지점에서 다른 모든 지점까지의 최단 경로를 계산

- 다익스트라 알고리즘
   : '단계마다 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드를 선택' 후,
   그 노드를 거쳐 가는 경우를 확인하여 최단거리를 갱신하는 방법
   : 우선순위 큐를 이용하여 소스코드 작성

- 플로이등 워셜 알고리즘
   : 다이나믹 프로그래밍을 이용하여 단계마다 '거쳐가는 노드'를 기준으로 최단거리 테이블을 갱신하는 방식
   - 점화식 : Dab = min(Dab, Dak + Dkb)
   for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                abj[a][b] = min(abj[a][b], abj[k][a] + abj[k][b])
'''

'''
# 플로이드 문제 (모든 정점에서 모든 정점으로의 최단 경로)
 - n개의 도시(100개 이하)
 - m개의 버스(100,000)
 - 시작도시 A, 도착도시 B, 필요한 비용 C
 - A -> B로 가는데 필요한 최소값
# Developer`s Kick!
 - A -> B 연결하는 간선이 여러 개일수 있음
 - 각각 비용 중 가장 짧은 간선 선택.

Input01
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

OutPut01
0 2 3 1 4
12 0 15 2 5
8 5 0 1 1
10 7 13 0 3
7 4 10 6 0

'''


def floyd():
    # 무한
    INF = 1e9

    # 노드의 개수와 간선의 개수를 입력받기
    n = int(input())
    m = int(input())

    # 2차원 리스트(그래프)를 만들고 모든 값을 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자신으로 가는 비용은 0으로 초기화
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선의 정보(버스)를 입력 받아 그 값으로 초기화
    for _ in range(m):

        # A에서 B로 가는 C의 비용
        a, b, c = map(int, input().split())

        # 가장 짧은 간선 정보 저장
        if c < graph[a][b]:
            graph[a][b] = c

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    # 결과물 출력
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if graph[a][b] == INF:
                print(0, end=" ")
            else:
                print(graph[a][b], end=" ")
        print()


'''
# 정확한 순위 문제
 - 학생의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하시오
 - N(학생의 수) / M(두 학생의 성적을 비교 횟수)
 - M번째 줄부터 두 학생의 성적을 비교한 결과를 나타냄 ex) A < B
# Developer`s Kick!
 - 최단경로를 계산하는 문제 = 최단 거리 알고리즘
 - A번 학생과 B번 학생의 성적을 비교할 때, '경로'를 이용하여 성적 비교 결과를 알 수 있음
 - A -> B로 도달이 가능하다는 것은 A가 B보다 성적이 낮음
 - A -> B || B -> A => '성적 비교' 가능

Input01
6 6
1 5
3 4
4 2
4 6
5 2
5 4

Output01 
1

'''


def rank():
    INF = 1e9

    # 노드의 개수, 간선의 개수 입력받기
    n, m = map(int, input().split())

    # 그래프를 만들고 무한으로 초기화
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
    for a in range(n + 1):
        for b in range(n + 1):
            if a == b:
                graph[a][b] = 0

    # 각 간선의 정보를 입력받아 그 값으로 초기화
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1

    # 점화식에 따라 플로이드 워셜 알고리즘 수행
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

    ret = 0
    # 각 학생을 번호에 따라 한 명씩 확이하며 도달 가능한지 체크
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] != INF or graph[j][i] != INF:
                cnt += 1
        if cnt == n:
            ret += 1
    print(ret)


if __name__ == "__main__":
    # floyd()
    rank()
