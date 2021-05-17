'''
# 구현문제
'''

'''
# 럭키스트레이트 문제
어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 
현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 
오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 
예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3,
오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.

현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 
럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다. 또한 점수 N의 자릿수는 항상 짝수 형태로만 주어진다. 
예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다.

# 입력
첫째 줄에 점수 N이 정수로 주어진다. (10 ≤ N ≤ 99,999,999) 단, 점수 N의 자릿수는 항상 짝수 형태로만 주어진다.

# 출력
첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다.

* Developer`s Kick!
String으로 입력 받을 것
왼쪽 오른쪽으로 나눠서 +- 하는 것!(summary)
summary == 0이라면 럭키스트레이트!

# Input     : 123402
# Output    : LUCKY
# Input     : 7755
# Output    : READY
'''


def lucky_straight():
    n = input()

    # 점수의 총자리 수
    length = len(n)
    summary = 0

    # 왼쪽 부분의 자리수 더하기
    for i in range(length // 2):
        summary += int(n[i])

    # 오른쪽 부분의 자리수 더하기
    for i in range(length // 2, length):
        summary -= int(n[i])

    if summary == 0:
        print("LUCKY")
    else:
        print("READY")


'''
알파벳 대문자와 숫자 (0~9)로만 구성된 문자열이 입력으로 주어집니다. 
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 
그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다. 
예를 들어 K1KA5CB7이 입력으로 들어오면, ABCKK13을 출력합니다.

* Developer`s Kick!
문자와 숫자를 나눠서 생각한다!
.isalpha를 활용한다!


# Input     : K1KA5CB7
# Output    : ABCKK13
# Input     : AJKDLSI412K4JSJ9D
# Output    : ADDIJJJKKLSS20
'''


def text_realign():
    data = input()
    ret = []
    value = 0

    for i in data:
        if i.isalpha():
            ret.append(i)
        else:
            value += int(i)

    ret.sort()

    if value != 0:
        ret.append(str(value))

    print(''.join(ret))


def text_compressed(s):
    answer = len(s)

    # 1개 단위(step)부터 압축단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""

        # 앞에서부터 step만큼 문자열 추출
        prev = s[0:step]
        cnt = 1

        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):

            # 이전 상태와 동일하다면, 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                cnt += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우)
            else:
                compressed += str(cnt) + prev if cnt >= 2 else prev
                # 다시 상태 초기화
                prev = s[j:j + step]
                cnt = 1

        # 남아 있는 문자열에 대해서 처리
        compressed += str(cnt) + prev if cnt >= 2 else prev

        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))

    return answer


'''
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 
열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 
또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다. 
열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 
매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 
열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.

# Developer`s Kick!
- 2차원 배열을 통한 완전탐색 문제!

'''


def rotate(key):
    # 행 길이 계산
    n = len(key)

    # 열 길이 계산
    m = len(key[0])

    # 결과 리스트
    rotate_key = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            rotate_key[j][n - i - 1] = key[i][j]
    return rotate_key


# 자물쇠의 중간 부분이 모두 1인지 확인
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

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        # 열쇠 회전
        key = rotate(key)

        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼어넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새루운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock):
                    return True

                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

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
    k = int(input())  # 사과 개수

    # 맵 정보
    data = [[0] * (n + 1) for _ in range(n + 1)]
    info = []  # 방향 회전 정보

    # 맵 정보( 사과가 있다면, 1로 표시 )
    for _ in range(k):
        a, b = map(int, input().split())
        data[a][b] = 1

    # 방향 회전 정보 표시
    l = int(input())
    for _ in range(l):
        x, c = input().split()
        info.append((int(x), c))

    # 처음에는 오른쪽을 향하고 있음 (동, 남, 서, 북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def turn(direction, c):
        if c == "L":
            direction = (direction - 1) % 4
        else:
            direction = (direction + 1) % 4
        return direction

    def simulate():
        x, y = 1, 1     # 뱀 머리 위치
        data[x][y] = 2  # 뱀이 존재하는 위치는 2로 표시!
        direction = 0   # 처음 보는 방향은 동쪽
        time = 0        # 시작한 뒤에 지난 '초' 단위 시간
        index = 0       # 다음에 회전할 정보
        q = [(x, y)]    # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

        while True:
            nx = x + dx[direction]
            ny = y + dy[direction]

            # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
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

            # 다음 위치로 머리 이동
            x, y = nx, ny
            time += 1
            # 회전할 시간인 경우, 회전.
            if index < l and time == info[index][0]:
                direction = turn(direction, info[index][1])
                index += 1
        return time

    print(simulate())


if __name__ == "__main__":
    # lucky_straight()
    # text_realign()
    # print(text_compressed("ababcdcdababcdcd"))
    # print(lock_key([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
    dummy_game()