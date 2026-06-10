class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Stores the frequency of prefix sums encountered
        # Base case: a prefix sum of 0 has been seen 1 time (empty subarray)
        prefix_sums = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # If (current_sum - k) exists in our map, it means we found
            # subarray(s) that sum up to k ending at the current index
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
                
            # Record the current prefix sum in the hash map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count