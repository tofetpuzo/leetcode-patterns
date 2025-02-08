# 39. Combination Sum
# Medium
# Topics
# Companies
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
# frequency
# of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.


# Example 1:

# Input: candidates = [2, 3, 6, 7], target = 7
# Output: [[2, 2, 3], [7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2, 3, 5], target = 8
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
# Example 3:

# Input: candidates = [2], target = 1
# Output: []


# Constraints:

# 1 <= candidates.length <= 30
# 2 <= candidates[i] <= 40
# All elements of candidates are distinct.
# 1 <= target <= 40
class Solution(object):
    def combination_sum(self, block_sizes, target_height):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        : block_sizes: a list of the heights of different blocks
        : target_heights: the desired height of the tower
        """

        tower_designs = []

        def explore_towers(current_tower: list, remaining_height, block_index):
            if remaining_height == 0:  # YAY! we built a tower of exactly the right height
                tower_designs.append(current_tower.copy())
                return

            if remaining_height < 0:  # oops! the tower is too tall, try something else
                return

            # now, let's try adding different blocks to the tower, one at a time.
            for i in range(block_index, len(block_sizes)):
                # add one of this block to the tower
                current_tower.append(block_sizes[i])

                # see if it works
                explore_towers(
                    current_tower, remaining_height - block_sizes[i], i)

                # take the block out so we can try something else
                current_tower.pop()

        explore_towers([], target_height, 0)

        return tower_designs


block_sizes = [2, 3, 5]
target_height = 9

tower_plans = Solution().combination_sum(block_sizes, target_height)

print(tower_plans)
