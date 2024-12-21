# 15. 3Sum
# Solved
# Medium
# Topics
# Companies
# Hint
# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.


# Example 1:

# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are[-1, 0, 1] and [-1, -1, 2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0, 1, 1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0, 0, 0]
# Output: [[0, 0, 0]]
# Explanation: The only possible triplet sums up to 0.


# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

def threeSum(nums: list[int]) -> list[list[int]]:
    """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res


# Time complexity: O(n^2)
# Space complexity: O(n)
# test case
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # [[-1, -1, 2], [-1, 0, 1]]


def alt_three_sum(nums: list[int]) -> list[list[int]]:
    """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n):
        if nums[i] > 0:
            break

        elif i > 0 and nums[i] == nums[i - 1]:
            continue

        lo, hi = i + 1, n - 1
        while lo < hi:
            summ = nums[i] + nums[lo] + nums[hi]
            if summ == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                lo, hi = lo + 1, hi - 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif summ < 0:
                lo += 1
            else:
                hi -= 1
    return res

# Time complexity: O(n^2)
# Space complexity: O(n)


# test case
numss = [-1, 0, 1, 2, -1, -4]
print(alt_three_sum(numss))  # [[-1, -1, 2], [-1, 0, 1]]
