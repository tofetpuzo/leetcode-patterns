# 1046. Last Stone Weight
# Easy
# Topics
# Companies
# Hint
# You are given an array of integers stones where stones[i] is the weight of the ith stone.

# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.


# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
# Example 2:

# Input: stones = [1]
# Output: 1


# Constraints:


# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000
def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """


# Time complexity: O(nlogn)

# Space complexity: O(n)

# tests

# Test case 1

stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))  # 1


# Test case 2

stones = [1]
print(lastStoneWeight(stones))  # 1


# Test case 3

stones = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
]
print(lastStoneWeight(stones))  # 0
