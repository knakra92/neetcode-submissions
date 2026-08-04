class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [None for _ in range(len(height))]
        max_right = [None for _ in range(len(height))]
        min_left_right = [None for _ in range(len(height))]

        current_max = 0
        for i in range(len(height)):
            max_left[i] = current_max
            if height[i] > current_max:
                current_max = height[i]
        
        current_max = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = current_max
            if height[i] > current_max:
                current_max = height[i]

        total_water = 0
        for i in range(len(height)):
            min_left_right[i] = min(max_left[i], max_right[i])
            c = min_left_right[i] - height[i]
            if c < 0:
                c = 0
            
            total_water += c

        print(max_left)
        print(max_right)
        print(min_left_right)

        return total_water
        

        
