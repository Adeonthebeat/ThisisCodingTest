'''
DFS/BFS 문제
- 탐색 : 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 자료구조 : '데이터를 표현하고 처리하는 방법'을 다룸
- 스택
 '박스 쌓기'에 비유
 선입후출 또는 후입선출 구조
- 큐
 대기줄에 비유
 선입선출 구조
- DFS
 '깊이 우선 탐색 알고리즘'이며, 그래프를 탐색하는 알고리즘
 DFS는 최대한 멀리 있는 노드를 우선으로 탐색하는 방식으로 동작하는 스택 자료구조를 이용
- BFS
 '너비우선탐색 알고리즘'
 가까운 노드부터 참색하는 알고리즘
 BFS는 선입선출 방식의 큐를 이용하면 구현 가능
 인접한 노드를 반복적으로 큐에 넣는 알고리즘을 작성하면
 자연스럽게 먼저 들어온 것은 먼저 나가가게 되어 가까운 노드부터 탐색
'''
from collections import deque
from itertools import combinations

'''
# 특정 거리의 도시 찾기
# Developer`s Kick!
 - 모든 도로의 거리는 1 = 모든 간선의 비용이 1
 - 모든 도로의 거리는 1이라는 조건 덕분에 너비우선탐색(BFS)을 이용해 간단히 해결!
 
Input1
4 4 2 1
1 2
1 3
2 3
2 4

Output1
4

Input2
4 3 2 1
1 2
1 3
1 4

Output2
-1

Input3
4 4 1 1
1 2
1 3
2 3
2 4

Output3
2
3

'''
def find_city():
    # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
    n, m, k, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)

    # 모든 도시에 대한 최단거리 초기화
    distance = [-1] * (n + 1)
    # 출발 도시까지의 거리는 0으로 설정
    distance[x] = 0

    # 너비우선탐색(BFS) 수행
    q = deque([x])
    while q:
        now = q.popleft()

        # 현재 도시에서 이동할 수 있는 모든 도시 확인
        for next_node in graph[now]:
            # 아직 방문하지 않은 도시라면.
            if distance[next_node] == -1:
                # 최단거리 갱신
                distance[next_node] = distance[now] + 1
                q.append(next_node)

    # 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
    check = False
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)
            check = True

    if check is False:
        print(-1)

'''
# 연구소 문제
0 : 빈칸
1 : 벽
2 : 바이러스
# Developer`s Kick!
 - 벽을 세 개 설치하는 경우의 모든 조합의 수 계산.
 - 조합 라이브러리 | DFS/BFS 사용

Input1
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

Output1
27

Input2
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

Output2
9

Input3
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

Output3
3

'''
def research_virus():

    # 지도의 맵
    n, m = map(int, input().split())

    # 초기 맵 리스트
    data = []

    # 벽을 설치한 뒤의 맵 리스트
    temp = [[0] * m for _ in range(n)]

    for _ in range(n):
        data.append(list(map(int, input().split())))

    # 4가지 이동방향에 대한 리스트
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    ret = 0

    # 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
    def virus(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
            if 0 <= nx < n and 0 <= ny < m:
                if temp[nx][ny] == 0:
                    # 해당 위치에 바이러스를 배치하고, 자시 재귀적으로 수행
                    temp[nx][ny] = 2
                    virus(nx, ny)

    # 현재 맵에서 안전 영역의 크기를 계산하는 메소드
    def get_score():
        score = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    score += 1
        return score

    # 깊이우선탐색(DFS)를 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
    def dfs(count):
        global ret

        # 울타리가 3개 설치된 경우
        if count == 3:
            for i in range(n):
                for j in range(m):
                    temp[i][j] = data[i][j]

            # 각 바이러스 위치에서 전파 진행
            for i in range(n):
                for j in range(m):
                    if temp[i][j] == 2:
                        virus(i, j)

            ret = max(ret, get_score())
            return

        for i in range(n):
            for j in range(m):
                if data[i][j] == 0:
                    data[i][j] = 1
                    count += 1
                    dfs(count)
                    data[i][j] = 0
                    count -= 1
    dfs(0)
    print(ret)


'''
# 경쟁적 전염 문제
 - N : 시험관 정보
 - K : 바이러스 정보
 - S : 시간(초)
# Developer`s Kick!
 - 너비우선탐색(BFS)를 이용한 문제
 - 각 바이러스는 낮은 번호부터 증식 ->> 큐에 낮은 바이러스의 번호부터 삽입
 - 너비우선탐색을 수행하여 방문하지 않은 위치를 차례대로 방문

Input1
3 3
1 0 2
0 0 0 
3 0 0
2 3 2

Output1
3

Input2
3 3
1 0 2
0 0 0 
3 0 0
1 2 2

Output2
0


'''
def infection():

    n, k = map(int, input().split())

    # 전체 보드 정보를 담는 리스트
    graph = []
    # 바이러스 정보를 담는 리스트
    data = []

    for i in range(n):
        # 보드 정보를 한 줄 단위로 입력
        graph.append(list(map(int, input().split())))
        for j in range(n):
            # 해당 위치에 바이러스가 존재할 경우
            if graph[i][j] != 0:
                # (바이러스 종류, 시간, 위치 X, 위치 Y) 삽입
                data.append((graph[i][j], 0, i, j))

    data.sort()
    q = deque(data)

    target_s, target_x, target_y = map(int, input().split())

    # 바이러스가 퍼져나갈 수 있는 4가지 위치
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        virus, s, x, y = q.popleft()
        # 정확하게 s초가 지나거나, 큐가 빌 때까지 반복
        if s == target_s:
            break

        # 현재 노드에서 주변 4가지 위치를 각각 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 해당 위치로 이동할 수 있는 경우
            if 0 <= nx < n and 0 <= ny < n:
                # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
                if graph[nx][ny] == 0:
                    graph[nx][ny] = virus
                    q.append((virus, s+1, nx, ny))

    print(graph[target_x - 1][target_y - 1])

'''
# 괄호변환 문제
 - 괄호가 올바른지 체크하는 문제
# Developer`s Kick!
 - 재귀적 함수 호출로 해결
'''
def parenthesis(p):

    # '균형 잡힌 괄호 문자열'의 인덱스 변환
    def balanced_index(p):
        # 왼쪽 괄호 개수
        cnt = 0
        for i in range(len(p)):
            if p[i] == '(':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                return i

    # '올바른 괄호 문자열'인지 체크
    def check_proper(p):
        # 왼쪽 괄호 개수
        cnt = 0
        for i in p:
            if i == '(':
                cnt += 1
            else:
                # 쌍이 맞지 않은 경우 False return
                if cnt == 0:
                    return False
                cnt -= 1
        return True

    def solution(p):
        answer = ''
        if p == '':
            return answer

        index = balanced_index(p)
        u = p[:index+1]     # 예를 들어 올바른 괄호 문자열이라면 v는 빈문자열이 될 수도 있음
        v = p[index+1:]


        # '올바른 괄호 문자열'이면, v에 대해 함수를 수행한 결과를 붙여 반환
        if check_proper(u):
            answer = u + solution(v)

        # '올바른 괄호 문자열'이 아니라면, 아래의 과정을 수행
        else:
            answer = '('
            answer += solution(v)
            answer += ')'
            # 첫번째와 마지막 문자를 제거
            u = list(u[1:-1])
            for i in range(len(u)):
                if u[i] == '(':
                    u[i] = ')'
                else:
                    u[i] = '('
            answer += "".join(u)

        return answer
    solution(p)

'''
# 연산자 끼어넣기
 - 연산자는 주어진 순서대로 함
 - 연산자 우선순위는 무시함
 - 만들 수 있는 식의 결과가 최대, 최소값을 구하세요
# Developer`s Kick!
 - 수가 주어졌을 때, 각 수와 수 사이에 사칙연산 중 하나를 삽입하는 모든 경우의 최대값, 최소값을 구하는 문제
 - 모든 경우의 수를 계산하기 위해 완전탐색 (DFS/BFS)를 이용하여 문제를 해결할 수 있음

Input1
2
5 6
0 0 1 0

Output1
30
30

Input2
3
3 4 5
1 0 1 0

Output2
35
17

Input3
6
1 2 3 4 5 6
2 1 1 1

Output3
54
-24
'''
def operator():

    # 수의 개수
    n = int(input())

    # 연산을 수행하고자 하는 수 리스트
    data = list(map(int, input().split()))

    # 연산자
    add, sub, mul, div = map(int, input().split())

    # 최소값, 최대값 초기화
    min_value = 1e9
    max_value = -1e9

    def dfs(i, now):
        global min_value, max_value, add, sub, mul, div

        # 모든 연산자를 다 사용한 경우, 최소값과 최대값 업데이트
        if i == n:
            min_value = min(min_value, now)
            max_value = max(max_value, now)

        else:
            # 각 연산자에 대하여 재귀적으로 수행
            if add > 0:
                add -= 1
                dfs(i + 1, now + data[i])
                add += 1
            if sub > 0:
                sub -= 1
                dfs(i + 1, now - data[i])
                sub += 1
            if mul > 0:
                mul -= 1
                dfs(i + 1, now * data[i])
                mul += 1
            if div > 0:
                div -= 1
                dfs(i + 1, int(now / data[i]))
                div += 1
    dfs(1, data[0])

    # 최대값, 최소값 차례대로 출력
    print(max_value)
    print(min_value)

'''
# 감시피하기 문제
 - S : student
 - T : teacher
 - O : obstacle
 - X : space
# Developer`s Kick!
 - 장애물을 정확히 3개 설치하는 모든 경우의 수를 확인하며, 모든 학생이 감시로부터 피하도록 할 수 있는지 여부를 출력
 - 복도의 크키는 N x N이며, N은 최대 6개
 - 장애물을 정확히 3개 설치하는 모든 조합의 수는 36C3이며, 10000개 이하의 수는 완전탐색으로 해결할 수 있음
 - DFS / BFS를 이용하여 문제를 해결
 
Input01
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

Output01
YES

Input02
4
S S S T
X X X X
X X X X
T T T X

Output02

'''
def surveilance():
    n = int(input())    # 복도의 크기
    board = []          # 복도 정보(NxN)
    teachers = []       # 모든 선생님의 위치 정보
    spaces = []         # 모든 빈 공간 위치 정보

    # 위치 정보 저장
    for i in range(n):
        board.append(list(input().split()))

        for j in range(n):
            # 선생님이 존재하는 위치 저장
            if board[i][j] == 'T':
                teachers.append((i, j))
            if board[i][j] == 'X':
                spaces.append((i, j))

    # 특정 방향으로 감시를 진행(학생 발견 : True / 학생 미발견 : False)
    def watch(x, y, direction):
        # 왼쪽 방향 감시
        if direction == 0:
            while y >= 0:
                # 학생이 있는 경우
                if board[x][y] == 'S':
                    return True
                # 장애물이 있는 경우
                if board[x][y] == 'O':
                    return False
                y -= 1
        # 오른쪽 방향 감시
        if direction == 1:
            while y < n:
                # 학생이 있는 경우
                if board[x][y] == 'S':
                    return True
                # 장애물이 있는 경우
                if board[x][y] == 'O':
                    return False
                y += 1
        # 위쪽 방향 감시
        if direction == 2:
            while x >= 0:
                # 학생이 있는 경우
                if board[x][y] == 'S':
                    return True
                # 장애물이 있는 경우
                if board[x][y] == 'O':
                    return False
                x -= 1
        # 아랫쪽 방향 감시
        if direction == 3:
            while x < n:
                # 학생이 있는 경우
                if board[x][y] == 'S':
                    return True
                # 장애물이 있는 경우
                if board[x][y] == 'O':
                    return False
                x += 1
        return False

    # 장애물 설치 후, 한명이라도 학생이 감지되는지 검사
    def process():
        # 모든 선생님의 위치를 하나씩 확인
        for x, y in teachers:
            # 4가지 방향으로 학생을 감지할 수 있는지 확인
            for i in range(n):
                if watch(x, y, i):
                    return True
        return False

    # 학생이 한 명도 감지되지 않도록 설치할 수 있는지 여부
    find = False

    # 빈 공간에서 3개를 뽑는 모든 조합 확인
    for data in combinations(spaces, 3):
        # 장애물 설치하기
        for x, y in data:
            board[x][y] = 'O'
        # 학생이 감지가 안 될 경우
        if not process():
            find = True
            break

        # 학생이 감지가 안 될 경우
        for x, y in data:
            board[x][y] = 'X'

    if find:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    # find_city()
    # research_virus()
    # infection()
    # parenthesis("()))((()")
    # operator()
    surveilance()