# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
#
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]


# 한 눈에 보는 동작 예시 (nums = [2, 7, 11, 15], target = 9)
# i = 0, 숫자 2를 확인:필요한 짝꿍: 9 - 2 = 7 장부(seen)에 7이 있는가? -> 없음 내 정보 기록: seen[2] = 0  (장부 상태: {2: 0})
# i = 1, 숫자 7을 확인:필요한 짝꿍: 9 - 7 = 2 장부(seen)에 2가 있는가? -> 있음! (인덱스 0에 있었음)정답 [0, 1] 반환 후 즉시 종료!

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        seen = {}  # {숫자: 인덱스} 형태로 저장할 장부

        for i, num in enumerate(nums):
            needed = target - num  # target을 만들기 위해 필요한 짝꿍 숫자

            # 필요한 숫자가 장부에 이미 적혀있다면, 정답.
            if needed in seen:
                return [seen[needed], i]

            # 없으면 나중에 올 숫자가 날 찾을 수 있게 내 숫자와 인덱스를 적어둠
            seen[num] = i

        return []


if __name__ == "__main__":
    sol = Solution()

    # Example 1 (기대 출력: [0, 1])
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Example 1 :", sol.twoSum(nums1, target1))

    # Example 2 (기대 출력: [1, 2])
    nums2 = [3, 2, 4]
    target2 = 6
    print("Example 2 :", sol.twoSum(nums2, target2))

    # Example 3 (기대 출력: [0, 1])
    nums3 = [3, 3]
    target3 = 6
    print("Example 3 :", sol.twoSum(nums3, target3))
