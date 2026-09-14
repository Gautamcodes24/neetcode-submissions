class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        # Initialize two pointers at the ends of the array
        left = 0
        right = len(arr) - 1
        
        # Shrink the window until it contains exactly k elements
        while right - left + 1 > k:
            # Compare distances to x
            # If the left element is further away, move the left pointer inward
            if abs(arr[left] - x) > abs(arr[right] - x):
                left += 1
            # If the right element is further away (or tied, prefer smaller element),
            # move the right pointer inward
            else:
                right -= 1
                
        # The remaining window of size k is the result
        return arr[left : right + 1]