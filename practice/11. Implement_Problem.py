'''
# 구현문제
'''

'''
# 럭키스트레이트 문제
어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.
특정 조건이란 현재 캐릭터의 점수를 N이라고 할 때 점수 N을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3,
오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.

현재 점수 N이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 럭키 스트레이트를 사용할 수 있다면 "LUCKY"를, 사용할 수 없다면 "READY"라는 단어를 출력한다. 또한 점수 N의 자릿수는 항상 짝수 형태로만 주어진다. 예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다.

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
    for i in range(length//2):
        summary += int(n[i])

    # 오른쪽 부분의 자리수 더하기
    for i in range(length//2, length):
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

if __name__ == "__main__":
    # lucky_straight()
    # text_realign()
    print(text_compressed("ababcdcdababcdcd"))