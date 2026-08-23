class Solution:
    def search(self, nums: List[int], target: int, offset=0) -> int:
        if not nums:
            return -1

        mid_idx = len(nums) // 2
        mid_num = nums[mid_idx]

        if mid_num == target:
            return offset + mid_idx

        elif target < mid_num:
            return self.search(nums[:mid_idx], target, offset)

        else:
            return self.search(nums[mid_idx+1:], target, offset + mid_idx + 1)
