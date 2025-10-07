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

# BEGINNER EXPLANATION:
# What this problem is asking: Find the shortest piece of string 's' that contains all characters from string 't' (including duplicates).
# Strategy (Sliding Window): 
# 1. EXPAND right pointer until window contains all characters from 't'
# 2. CONTRACT left pointer while maintaining all characters (find minimum)
# 3. REPEAT until we've checked all possibilities
# Think of it like adjusting a rubber band around letters on a table - stretch it right until you capture everything you need, then squeeze it left as much as possible while keeping everything inside!

# Import helpful tools:
# Counter: Counts how many times each character appears in a string
# defaultdict: A dictionary that gives you 0 when you ask for a key that doesn't exist yet
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # If either string is empty, return empty string (no solution possible)
        if not s or not t:
            return ""

        # Count all characters in 't'. Example: if t = "ABC", then dict_t = {'A': 1, 'B': 1, 'C': 1}
        dict_t = Counter(t)
        
        # How many unique characters we need to find. Example: for t = "ABC", we need 3 unique characters
        required = len(dict_t)

        # Create two pointers (like fingers pointing at positions):
        # l = left pointer (start of our window), r = right pointer (end of our window)
        l, r = 0, 0
        
        # Counter for how many unique characters we've satisfied so far
        # We increment this when we have enough of a character
        formed = 0
        
        # Keep track of character counts in our current window
        # Starts at 0 for any character we haven't seen
        window_counts = defaultdict(int)

        # Store our best answer so far: (window_length, left_position, right_position)
        # float("inf") = infinity (very large number)
        ans = float("inf"), None, None  # window length, left, right

        # Keep expanding our window to the right until we reach the end
        while r < len(s):
            # Get the character at position 'r' and add 1 to its count in our window
            character = s[r]
            window_counts[character] += 1

            # Check if we just satisfied a character requirement:
            # - Is this character needed in 't'?
            # - Do we now have exactly the right amount?
            # - If yes, increment 'formed' (we satisfied one more unique character)
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # While our window contains all required characters, try to shrink it from the left
            while l <= r and formed == required:
                # Get the character we're about to remove from the left
                character = s[l]

                # If current window is smaller than our best answer:
                # r - l + 1 = current window size
                # Update our best answer with current window info
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # Remove the left character from our window count
                window_counts[character] -= 1
                
                # Check if removing this character broke a requirement:
                # - Was this character needed?
                # - Do we now have too few of it?
                # - If yes, decrement 'formed' (we no longer satisfy this character)
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move left pointer right (shrink window from left)
                l += 1    

            # Move right pointer right (expand window)
            r += 1    

        # Return the result:
        # - If we never found a valid window, return empty string
        # - Otherwise, return the substring from our best answer
        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
        

