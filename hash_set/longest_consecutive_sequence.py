# 28. Longest Consecutive Sequence
# Medium
# Topics
# Companies
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


# Example 1:

# Input: nums = [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 9


# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109
class Solution(object):
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                next_num = num + 1
                current_length = 1
                while next_num in nums_set:
                    current_length += 1
                    next_num += 1
                max_length = max(max_length, current_length)

        return max_length


# Time complexity: O(N)
# Space complexity: O(N)
# Approach: Hash Set
# The idea is to convert the given array into a set.
# This is done to make the search operation in the set to be O(1).
# We then iterate through the set and for each element, we check if the element - 1 is in the set.
# If it is not, then we start a new sequence from the current element.
# We then keep incrementing the current element by 1 and check if the incremented element is in the set.
# If it is, then we increment the current length of the sequence.
# We then update the maximum length of the sequence.
# We return the maximum length of the sequence.
# This algorithm runs in O(N) time complexity.
# This is because we iterate through the set only once.
# The space complexity of this algorithm is O(N).


# test cases
# 1. empty array
# 2. array with one element
# 3. array with multiple elements


nums = [100, 4, 200, 1, 3, 2]
# Output: 4
print(Solution().longest_consecutive(nums))
