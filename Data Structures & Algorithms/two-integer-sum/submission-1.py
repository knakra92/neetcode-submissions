class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_tracker: dict[int, int] = {}

        for idx, n in enumerate(nums):
            num_tracker[n] = idx
        print(num_tracker)
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in num_tracker and idx != num_tracker[diff]:
                return [idx, num_tracker[diff]]

        return []