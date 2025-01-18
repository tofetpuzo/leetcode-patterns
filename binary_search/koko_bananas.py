# 875. Koko Eating Bananas
# Medium
# Topics
# Companies
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:


# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        def possible(K):
            return sum((p - 1) // K + 1 for p in piles) <= h

        l, r = 1, max(piles)
        while l < r:
            m = (l + r) // 2
            if not possible(m):
                l = m + 1
            else:
                r = m
        return l


# Time: O(nlogm)
# Space: O(1)

piles = [3, 6, 7, 11]
h = 8
# Output: 4
print(Solution().minEatingSpeed(piles, h))

# 1. We can binary search the answer. The answer is between 1 and max(piles).
