# 46.Permutation(순열)

# 순서가 있는 모든 조합

# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]

# Example 3:
# Input: nums = [1]
# Output: [[1]]

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        # 모든 순열 결과를 담을 최종 반환 리스트
        result = []

        # 각 인덱스의 숫자를 현재 사용 중인지 체크하는 방문 배열 (초기값 전부 False)
        visited = [False] * len(nums)

        # 백트래킹을 수행할 재귀 함수 (current: 지금까지 고른 숫자들을 담는 임시 리스트)
        def backtrack(current: list[int]):
            # 1. 기저 조건: 고른 숫자의 개수가 원래 배열길이와 같아지면 하나의 순열 완성
            # len(current) == len(nums): 예를 들어 nums가 3개짜리면, current에 숫자가 3개 찼을 때 하나의 완전한 순열이 완성된 것
            if len(current) == len(nums):
                # 완성된 현재 상태의 스냅샷을 저장하고 재귀 종료
                result.append(current[:])
                return

            # 2. nums 배열의 모든 숫자를 순차적으로 후보 고려
            for i in range(len(nums)):
                # 아직 사용하지 않은 숫자만 선택
                if not visited[i]:
                    # 선택단계
                    visited[i] = True  # i번째 숫자를 사용중으로 표시
                    current.append(nums[i])  # 현재 순열에 숫자 추가

                    # 탐색단계
                    backtrack(current)

                    current.pop()
                    visited[i] = False

        # 빈바구니 상태로 백트래킹 시작 = 첫실행
        backtrack([])

        # 생성된 모든 순열리스트 반환
        return result


if __name__ == "__main__":
    sol = Solution()

    # 테스트 케이스 1
    # 기대 출력: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    nums1 = [1, 2, 3]
    print("Example 1 :", sol.permute(nums1))

    # 테스트 케이스 2
    # 기대 출력: [[0, 1], [1, 0]]
    nums2 = [0, 1]
    print("Example 2 :", sol.permute(nums2))

    # 테스트 케이스 3
    # 기대 출력: [[1]]
    nums3 = [1]
    print("Example 3 :", sol.permute(nums3))
