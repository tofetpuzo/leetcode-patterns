# 17. Letter Combinations of a Phone Number
# Medium
# Topics
# Companies
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

# A mapping of digits to letters(just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


# Example 1:

# Input: digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
# Example 2:

# Input: digits = ""
# Output: []
# Example 3:

# Input: digits = "2"
# Output: ["a", "b", "c"]


# Constraints:

# 0 <= digits.length <= 4
# digits[i] is a digit in the range['2', '9'].
class Solution(object):
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res, sol = [], []

        def backtrack(start):
            if len(sol) == len(digits):
                res.append(''.join(sol))
                return
            for i in range(start, len(digits)):
                for j in phone[digits[i]]:
                    sol.append(j)
                    backtrack(i + 1)
                    sol.pop()

        backtrack(0)
        return res

# Time complexity: O(4^N) where N is the number of digits in the input
# Space complexity: O(4^N) since we have 4^N combinations

# Approach: Backtracking
# The idea is to generate all the combinations of the given phone number.
# We can do this by using backtracking.
# We start by creating an empty list called combinations.
# We then call the backtrack function with the given phone number, an empty path list,
# and the combinations list.
# The backtrack function is a recursive function that takes the phone number,
# the current path, and the combinations list as arguments.

# If the path list has the same length as the phone number, we add the current path to the combinations list and return.

# Otherwise, we iterate over the phone number and add the current element to the path list.

# We then call the backtrack function with the updated path list and the combinations list.


# test cases
digits = "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
print(Solution().letter_combinations(digits))


# approach: Iterative

def letter_combinations(digits):
    if not digits:
        return []

    lettr_map = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    res, sol = [], []

    n = len(digits)

    def backtrack(i):
        if i == n:
            res.append(''.join(sol))
            return
        for j in lettr_map[digits[i]]:
            sol.append(j)
            backtrack(i + 1)
            sol.pop()
    backtrack(0)

    return res

# Time complexity: O(4^N) where N is the number of digits in the input
# Space complexity: O(4^N) since we have 4^N combinations
