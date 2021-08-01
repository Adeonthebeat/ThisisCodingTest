import heapq
import sys
import string
import numpy
import textwrap

###########################################################
# 자동 코드 정렬 ctrl +alt + i
from scipy.stats import ansari

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
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

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

    for i in range(1, n + 1):
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
        for i in range(1, n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstras(start):
        distance[start] = 0
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]

        for i in range(n - 1):
            now = get_smallest_node()  # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
            visited[now] = True
            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost

    dijkstras(start)

    for i in range(1, n + 1):
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
        heapq.heappush(q, (food_times[i], i + 1))

    while sum_value + (q[0][0] - previous) * length <= k:
        # 음식
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length

        length -= 1
        previous = now

    ret = sorted(q, key=lambda x: x[1])
    return ret[(k - sum_value) % length][1]


def lucky_straight():
    data = input()

    length = len(data) // 2

    ret = 0

    # Left
    for i in range(length):
        ret += int(data[i])

    # Right
    for i in range(length, len(data)):
        ret -= int(data[i])

    if ret == 0:
        print("LUCKY")
    else:
        print("READY")


def text_realign():
    s = input()

    ret = []
    num = 0
    for i in s:
        if i.isalpha():
            ret.append(i)
        else:
            num += int(i)
    ret.sort()

    if num != 0:
        ret.append(str(num))

    print(''.join(ret))


def text_compreesed(s):
    answer = len(s)

    # step부터 압축단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]  # 앞에서부터 step만큼 문자열 추출
        count = 1

        # 단위 크기만큼 증가시키면서 이전 단어와 비교
        for j in range(step, len(s), step):
            # 이전상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]  # 상태 초기화
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer


def rotate(key):
    n = len(key)  # 행
    m = len(key[0])  # 열

    rotate_key = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotate_key[j][n - i - 1] = key[i][j]
    return rotate_key


def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def lock_key(key, lock):
    n = len(lock)
    m = len(key)

    # 새로운 자물쇠의 중앙부분에 기존의 자물쇠 넣기
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):

        # 열쇠 회전
        rotated_key = rotate(key)

        # 자물쇠
        for x in range(n * 2):
            for y in range(n * 2):

                # 자물쇠에 열쇠 끼어넣기(key)
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += rotated_key[i][j]

                if check(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= rotated_key[i][j]
    return False


'''
'Dummy' 라는 도스게임이 있다. 이 게임에는 뱀이 나와서 기어다니는데, 사과를 먹으면 뱀 길이가 늘어난다. 뱀이 이리저리 기어다니다가 벽 또는 자기자신의 몸과 부딪히면 게임이 끝난다.
게임은 NxN 정사각 보드위에서 진행되고, 몇몇 칸에는 사과가 놓여져 있다. 보드의 상하좌우 끝에 벽이 있다. 게임이 시작할때 뱀은 맨위 맨좌측에 위치하고 뱀의 길이는 1 이다. 뱀은 처음에 오른쪽을 향한다.
뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따른다.
먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
사과의 위치와 뱀의 이동경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하라.
'''
'''
# Input :
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

# Output :
9

# Input :
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

# Output :
21

# Input :
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

# Output :
13
'''


def dummy_game():
    n = int(input())  # 보드의 크기
    k = int(input())  # 사과의 개수

    # 맵 정보
    data = [[0] * (n + 1) for _ in range(n + 1)]

    # 방향 회전 정보
    info = []

    # 맵 정보(사과 있는 곳 : 1)
    for _ in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1

    # 방향 회전 정보 입력
    l = int(input())
    for _ in range(l):
        x, c = input().split()
        info.append((int(x), c))

    # 처음에는 오른쪽을 보고 있음(동, 남, 서, 북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn(direction, c):
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        return direction

    def simulate():
        x, y = 1, 1  # 뱀의 머리 위치
        data[x][y] = 2  # 뱀이 존재하는 위치는 2
        direction = 0  # 처음에는 동쪽을 보고 있음
        time = 0  # 시작한 뒤에 지난 '초' 시간
        index = 0  # 다음에 회전할 정보
        q = [(x, y)]  # 뱀이 차지하고 있는 위치정보(꼬리가 앞쪽)

        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치
            if 1 <= nx <= n and 1 <= ny <= n and data[nx][ny] != 2:

                # 사과가 없다면, 이동 후에 꼬리 제거
                if data[nx][ny] == 0:
                    data[nx][ny] = 2
                    q.append((nx, ny))
                    px, py = q.pop(0)
                    data[px][py] = 0
                # 사과가 있다면, 이동 후에 꼬리 그대로 두기
                if data[nx][ny] == 1:
                    data[nx][ny] = 2
                    q.append((nx, ny))
            # 벽이나 뱀의 몸통과 부딪혔다면
            else:
                time += 1
                break

            # 다음 위치로 머리를 이동
            x, y = nx, ny
            time += 1
            if index < l and time == info[index][0]:
                direction = turn(direction, info[index][1])
                index += 1
        return time

    print(simulate())


def solution(answers):
    answer = []

    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    c1, c2, c3 = 0, 0, 0
    # [1, 3, 2, 4, 2]
    for i in range(len(answers)):
        if answers[i] == a1[i % len(a1)]:
            c1 += 1
        if answers[i] == a2[i % len(a2)]:
            c2 += 1
        if answers[i] == a3[i % len(a3)]:
            c3 += 1

    tmp = [c1, c2, c3]

    for num, score in enumerate(tmp):
        print(num, score, max(tmp))
        if score == max(tmp):
            answer.append(num + 1)

    return answer


if __name__ == "__main__":
    # Dijkstras()
    # Dijkstras_HEAP()
    # Choose_BowlingBall()
    # lucky_straight()
    # text_realign()
    # print(text_compreesed("ababcdcdababcdcd"))
    # dummy_game()
    print(solution(	[1, 3, 2, 4, 2]))
