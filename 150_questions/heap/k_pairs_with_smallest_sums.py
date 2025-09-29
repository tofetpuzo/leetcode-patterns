# 373. Find K Pairs with Smallest Sums
# Medium
# Topics
# conpanies icon
# Companies
# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

# Define a pair (u, v) which consists of one element from the first array and one element from the second array.

# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
 

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length

from heapq import heappop, heappush, heapify

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        """
        Example walkthrough with nums1 = [1,7,11], nums2 = [2,4,6], k = 3:
        
        Step 1: Initialize heap with first element from nums2 paired with first min(k, len(nums1)) elements from nums1
        min(3, 3) = 3, so we consider all elements from nums1
        
        Initial heap: [(3, 0, 0), (9, 1, 0), (13, 2, 0)]
        - (1+2=3, i=0, j=0) -> pair [1,2]
        - (7+2=9, i=1, j=0) -> pair [7,2] 
        - (11+2=13, i=2, j=0) -> pair [11,2]
        """
        min_heap = []
        
        # Initialize heap with pairs using first element of nums2
        # min(k, len(nums1)) ensures we don't add more than k starting pairs
        # and don't exceed nums1 length
        for i in range(min(k, len(nums1))):
            # Push (sum, index_in_nums1, index_in_nums2)
            heappush(min_heap, (nums1[i] + nums2[0], i, 0))
            # After each iteration:
            # i=0: heap = [(3, 0, 0)]
            # i=1: heap = [(3, 0, 0), (9, 1, 0)]  
            # i=2: heap = [(3, 0, 0), (9, 1, 0), (13, 2, 0)]
        
        result = []
        
        # Extract k smallest pairs
        while k > 0 and min_heap:
            # Pop the pair with minimum sum
            curr_sum, i, j = heappop(min_heap)
            # Iteration 1: curr_sum=3, i=0, j=0 -> pair [1,2]
            # Iteration 2: curr_sum=5, i=0, j=1 -> pair [1,4] 
            # Iteration 3: curr_sum=7, i=0, j=2 -> pair [1,6]
            
            result.append([nums1[i], nums2[j]])
            # After each iteration:
            # result = [[1,2]]
            # result = [[1,2], [1,4]]
            # result = [[1,2], [1,4], [1,6]]
            
            # If there's a next element in nums2, add the next pair with same nums1[i]
            if j + 1 < len(nums2):
                heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
                # Iteration 1: Add (1+4=5, 0, 1) -> heap = [(5, 0, 1), (9, 1, 0), (13, 2, 0)]
                # Iteration 2: Add (1+6=7, 0, 2) -> heap = [(7, 0, 2), (9, 1, 0), (13, 2, 0)]
                # Iteration 3: j+1 = 3, which >= len(nums2)=3, so nothing added
            
            k -= 1
            # k becomes: 2, 1, 0
        
        return result
        # Final result: [[1,2], [1,4], [1,6]]
