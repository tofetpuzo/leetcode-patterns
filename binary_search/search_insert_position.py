# 5. Search Insert Position
# Solved
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not ,
# return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return l

# Time complexity: O(log n)
# Space complexity: O(1)

# test case
nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums, target))  # 2


nums2 = [1, 3, 5, 6]
target2 = 2
print(searchInsert(nums2, target2))  # 1

