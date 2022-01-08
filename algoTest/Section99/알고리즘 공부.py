
# 해시
import collections
def solution(participant, completion):
    answer = ''

    answer = collections.Counter(participant) - collections.Counter(completion) 
    
    return list(answer.keys())[0]

# 해시
def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book)
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            answer = False
    
    
    return answer

# 큐
from collections import deque

def solution(progresses, speeds):
    answer = []

    progresses = deque(progresses)
    speeds = deque(speeds)


    while progresses:

        while progresses[0] < 100:
            for i in range(len(progresses)):
                progresses[i] += speeds[i]

        cnt = 0
        while progresses:
            if progresses[0] >= 100:
                cnt +=1
                progresses.popleft()
                speeds.popleft()

            else:
                break

        answer.append(cnt)
    return answer

# 큐
from collections import deque
def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer    


# 정렬
def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        
        temp = array[commands[i][0] - 1:commands[i][1]]
        temp.sort()
        answer.append(temp[commands[i][2] - 1])
    
    return answer

# 정렬
def solution(numbers):
    
    
    num = list(map(str, numbers))
    # 변환된 num을 sort()를 사용하여 key 조건에 맞게 정렬한다.
    # lambda x: x * 3은 num 인자인 각각의 문자열을 3번 반복을 의미

    num.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(num)))
    
    return answer