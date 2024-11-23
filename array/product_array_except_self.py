# 238. Product of Array Except Self
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
def product_except_self(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    output = [1] * len(nums)
    left = 1
    for i in range(1, len(nums)):
        left *= nums[i - 1]
        output[i] *= left
    right = 1
    for i in range(len(nums) - 2, -1, -1):
        right *= nums[i + 1]
        output[i] *= right
    return output

# Time: O(n)
# Space: O(1)

# Test case
nums = [1,2,3,4]

print(product_except_self(nums))  # [24,12,8,6]
    
    