# 918. Maximum Sum Circular Subarray
# Medium
# Topics
# conpanies icon
# Companies
# Hint
# Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

# Example 1:

# Input: nums = [1,-2,3,-2]
# Output: 3
# Explanation: Subarray [3] has maximum sum 3.
# Example 2:

# Input: nums = [5,-3,5]
# Output: 10
# Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
# Example 3:

# Input: nums = [-3,-2,-3]
# Output: -2
# Explanation: Subarray [-2] has maximum sum -2.
 

# Constraints:

# n == nums.length
# 1 <= n <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_current = max_global = arr[0]
            for num in arr[1:]:
                max_current = max(num, max_current + num)
                max_global = max(max_global, max_current)
            return max_global

        total_sum = sum(nums)
        max_kadane = kadane(nums)

        # Invert the array to find the minimum subarray sum
        inverted_nums = [-num for num in nums]
        min_subarray_sum = kadane(inverted_nums)

        max_wrap = total_sum + min_subarray_sum  # total - (-min_subarray_sum)

        # If all numbers are negative, max_wrap becomes 0 (invalid)
        if max_wrap == 0:
            return max_kadane

        return max(max_kadane, max_wrap)
    
    
print(Solution.maxSubarraySumCircular([1, -2, 3, -2]))  # Output: 3
print(Solution.maxSubarraySumCircular([5, -3, 5]))      # Output: 10
print(Solution.maxSubarraySumCircular([-3, -2, -3]))    # Output: -2

