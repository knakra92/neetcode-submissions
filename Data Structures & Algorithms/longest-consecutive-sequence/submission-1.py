class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        unique_nums: set = set()

        for n in nums:
            if n not in unique_nums:
                unique_nums.add(n)

        max_seq = 1
        
        for n in nums:
            if n-1 not in unique_nums:
                counter = 1
                while n+1 in unique_nums:
                    counter += 1
                    n += 1

                max_seq = max(counter, max_seq)

        return max_seq
