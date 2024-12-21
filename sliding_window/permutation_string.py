# 567. Permutation in String
# Medium
# Topics
# Companies
# Hint
# Given two strings s1 and s2, return true if s2 contains a 
# permutation
#  of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 1.1M
# Submissions
# 2.4M
# Acceptance Rate
# 46.6%
# Topics
# Companies
# Hint 1
# Hint 2
# Hint 3
# Hint 4
# Hint 5
# Hint 6
# Similar Questions
# Discussion (233)

# Choose a type


def check_inclusion(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    n1 = len(s1)
    n2 = len(s2)
    
    if n1 > n2:
        return False
    
    s1_count = [0] * 26
    s2_count = [0] * 26
    
    for i in range(n1):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1
        
    if s1_count == s2_count:
        return True
    
    for i in range(n1, n2):
        s2_count[ord(s2[i]) - ord('a')] += 1
        s2_count[ord(s2[i - n1]) - ord('a')] -= 1
        if s1_count == s2_count:
            return True
    return False


