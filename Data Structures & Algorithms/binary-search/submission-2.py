class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, target, 0, len(nums) - 1)

    def _search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self._search(nums, target, left, mid - 1)
        else:
            return self._search(nums, target, mid + 1, right)
