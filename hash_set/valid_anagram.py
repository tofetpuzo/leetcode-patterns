# 242. Valid Anagram
# Easy
# Topics
# Companies
# Given two strings s and t, return true if t is an
# anagram
#  of s, and false otherwise.


# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false


# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import defaultdict

        info = defaultdict(int)
        rans = defaultdict(int)

        for letter in s:
            info[letter] += 1

        for i in t:
            rans[i] += 1

        return rans == info
