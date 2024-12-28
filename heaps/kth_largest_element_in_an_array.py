# 215. Kth Largest Element in an Array
# Attempted
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Can you solve it without sorting?


# Example 1:

# Input: nums = [3, 2, 1, 5, 6, 4], k = 2
# Output: 5
# Example 2:

# Input: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
# Output: 4


# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104
def findKthLargest(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: int
    """
    from heapq import heapify, heappop

    for i in range(len(nums)):
        nums[i] *= -1

    heapify(nums)

    for i in range(k - 1):
        heappop(nums)

    return -heappop(nums)


# Time complexity: O(nlogn)

# Space complexity: O(n)

# tests

# Test case 1

nums = [3, 2, 1, 5, 6, 4]

k = 2
print(findKthLargest(nums, k))  # 5


# approach 2 using min heap with size k
def findKthLargest(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: int
    """
    from heapq import heapify, heappush, heappushpop

    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        else:
            heappushpop(min_heap, num)

    return min_heap[0]
