# 242. Valid Anagram
# Solved
# Easy
# Topics
# conpanies icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters?
# How would you adapt your solution to such a case?

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
        
# Follow up: What if the inputs contain Unicode characters?
# How would you adapt your solution to such a case?
# The current solution already handles Unicode characters since Python's strings are Unicode by default.
# The dictionary will correctly count occurrences of any Unicode character.