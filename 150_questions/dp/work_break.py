# 139. Word Break
# Medium
# Topics
# conpanies icon
# Companies
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

# Example 1:

# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
# Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false

# Constraints:

# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        # dp[i] represents whether s[0:i] can be segmented using words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented

        # For each position i in the string
        for i in range(1, len(s) + 1):
            # Check all possible split points j before position i
            for j in range(i):
                # If s[0:j] can be segmented AND s[j:i] is a valid word
                # then s[0:i] can be segmented
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # Found one valid segmentation, no need to check more

        return dp[len(s)]  # Return whether the entire string can be segmented
# WHY THIS WORKS:
# We use dynamic programming where dp[i] tells us if substring s[0:i] can be broken into words.
# For each position i, we try all possible previous positions j and check:
# 1. Can s[0:j] be segmented? (dp[j] == True)
# 2. Is s[j:i] a valid word? (s[j:i] in wordSet)
# If both are true, then s[0:i] can be segmented.
#
# EXAMPLE: s = "leetcode", wordDict = ["leet","code"]
# dp = [T, F, F, F, F, F, F, F, F]  # Initially only dp[0] = True
# i=1: s[0:1]="l" → no valid split → dp[1] = False
# i=2: s[0:2]="le" → no valid split → dp[2] = False  
# i=3: s[0:3]="lee" → no valid split → dp[3] = False
# i=4: s[0:4]="leet" → j=0: dp[0]=True and s[0:4]="leet" in wordSet → dp[4] = True
# i=5: s[0:5]="leetc" → no valid split → dp[5] = False
# i=6: s[0:6]="leetco" → no valid split → dp[6] = False
# i=7: s[0:7]="leetcod" → no valid split → dp[7] = False  
# i=8: s[0:8]="leetcode" → j=4: dp[4]=True and s[4:8]="code" in wordSet → dp[8] = True
#
# Time Complexity: O(n^2) where n is the length of the string s
# Space Complexity: O(n) for the dp array and O(m) for the wordSet
