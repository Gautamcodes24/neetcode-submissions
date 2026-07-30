class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findVal(arr):
            l = 0
            r = len(arr) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        ROWS = len(matrix)
        l = 0
        r = ROWS - 1
        while l <= r:
            mid = l + (r-l) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return findVal(matrix[mid])
            elif matrix[mid][-1] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False