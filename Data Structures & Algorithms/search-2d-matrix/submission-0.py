from typing import List, Tuple

class Solution:
    def find_row(self, matrix: List[List[int]], target) -> Tuple[int, bool]:
        if not matrix or not matrix[0]:
            return (0, False)
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            mid = top + (bottom - top) // 2
            first = matrix[mid][0]
            if first == target:
                return (mid, True)
            elif first < target:
                top = mid + 1
            else:
                bottom = mid - 1

        # bottom is the index of the row whose first element <= target (or -1 if target < first element)
        if bottom < 0:
            return (0, False)
        return (bottom, False)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row, found = self.find_row(matrix, target)
        if found:
            return True

        left = 0
        right = len(matrix[row]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[row][mid]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False