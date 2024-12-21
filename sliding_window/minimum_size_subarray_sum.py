# 209. Minimum Size Subarray Sum
# Medium
# Topics
# Companies
# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a
# subarray
# whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
# Output: 2
# Explanation: The subarray[4, 3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1, 4, 4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
# Output: 0


# Constraints:

# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.3M
# Submissions
# 2.6M
# Acceptance Rate
# 48.3%



def minSubArrayLen(target, nums):
    """
        :type target: int
        :type nums: List[int]
        :rtype: int
    """
    l = 0
    n = len(nums)
    total_sum = 0
    min_len = float('inf')
    for r in range(n):
        total_sum += nums[r]
        while total_sum >= target:
            min_len = min(min_len, r - l + 1)
            total_sum -= nums[l]
            l += 1
    return min_len if min_len != float('inf') else 0

 

# Time: O(N)

# Space: O(1)

print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3])) # 2

print(minSubArrayLen(4, [1, 4, 4])) # 1

    
    
    
