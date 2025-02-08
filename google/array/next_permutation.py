# 31. Next Permutation
# Solved
# Medium
# Topics
# Companies
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.


# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]


# Constraints:

# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # 1. Find the "dip" (the first decreasing element from right to left)
        i = n - 2  # Start from second-to-last element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:  # If a "dip" was found
            # 2. Find the smallest element to the right that's larger than nums[i]
            j = n - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1

            # 3. Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

            # 4. Reverse the suffix after index i
        # If i is -1, it means we didn't find a "dip," and the array is in reverse order already.
        # In this case, we still need to reverse the whole list.
        nums[i + 1 :] = reversed(nums[i + 1 :])
