# 1004. Max Consecutive Ones III
# Medium
# Topics
# Companies
# Hint
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


# Example 1:

# Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2
# Output: 6
# Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# Example 2:

# Input: nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k = 3
# Output: 10
# Explanation: [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
# 0 <= k <= nums.length

def longest_ones(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: int
    """
    max_window = 0
    num_zeroes = 0
    l = 0

    for r in range(len(nums)):
        if nums[r] == 0:
            num_zeroes += 1

        while num_zeroes > k:
            if nums[l] == 0:
                num_zeroes -= 1
            l += 1

        max_window = max(max_window, r - l + 1)

    return max_window

# Time complexity: O(n)

# Space complexity: O(1)

# test case
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longest_ones(nums, k))  # 6

