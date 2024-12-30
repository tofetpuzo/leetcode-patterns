# 347. Top K Frequent Elements
# Solved
# Medium
# Topics
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1, 1, 1, 2, 2, 3], k = 2
# Output: [1, 2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range[1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.


# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
from collections import Counter
from heapq import heappush, heappop

def topKFrequent(nums, k):
    """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
    """
    # step 1: count the frequency of each element
    count = Counter(nums)

    # step 2: use a min heap to keep track of k most frequent elements
    heap = []
    for num , freq in count.items():
        heappush(heap, (freq, num))
        if len(heap) > k:
            heappop(heap)

    # step 3: return the k most frequent elements
    res = [num for freq, num in heap]
    return res

# Time complexity: O(n log k)
# Space complexity: O(n)

# test case
nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))  # [1, 2]



