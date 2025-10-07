# 76. Minimum Window Substring
# Solved
# Hard
# Topics
# conpanies icon
# Companies
# Hint
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.

 

# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
# Example 2:

# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
# Example 3:

# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
 

# Constraints:

# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.
# hints: Use two pointers to create a window of letters in s, 
# which would have all the characters from t.
# Expand the right pointer until all the characters of t are covered.
# Sliding Window
# Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.
# Continue expanding the right and left pointers until you reach the end of s.
# Hash Table

from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        l, r = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        ans = float("inf"), None, None  # window length, left, right

        while r < len(s):
            character = s[r]
            window_counts[character] += 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                l += 1    

            r += 1    

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
        

