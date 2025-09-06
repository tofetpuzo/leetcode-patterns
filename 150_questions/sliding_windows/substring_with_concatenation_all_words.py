# 30. Substring with Concatenation of All Words
# Hard
# Topics
# conpanies icon
# Companies
# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]

# Output: [0,9]

# Explanation:

# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

# Output: []

# Explanation:

# There is no concatenated substring.

# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

# Output: [6,9,12]

# Explanation:

# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        # Step 1: Handle edge cases and get basic measurements
        if not s or not words or not words[0]:
            return []
        
        word_len = len(words[0])  # Length of each word
        total_words = len(words)  # Number of words
        total_len = word_len * total_words  # Total length of concatenated string
        
        # If string is shorter than total length needed, no solution
        if len(s) < total_len:
            return []
        
        # Step 2: Create frequency map of words we need to find
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        result = []
        
        # Step 3: Only need to check word_len different starting positions
        # This is the key optimization - instead of checking every position,
        # we only check positions 0, 1, 2, ..., word_len-1
        for i in range(word_len):
            self._sliding_window_check(s, i, word_len, total_words, word_count, result)
        
        return result
    
    def _sliding_window_check(self, s, start, word_len, total_words, word_count, result):
        """
        Use sliding window to check all possible concatenations starting at positions
        start, start + word_len, start + 2*word_len, etc.
        """
        seen = {}  # Count of words in current window
        left = start  # Left boundary of window
        
        # Slide through string with step size = word_len
        for right in range(start, len(s) - word_len + 1, word_len):
            # Extract current word
            word = s[right:right + word_len]
            
            # If word is not in our target words, reset window
            if word not in word_count:
                seen.clear()
                left = right + word_len
                continue
            
            # Add word to current window
            seen[word] = seen.get(word, 0) + 1
            
            # If we have too many of this word, shrink window from left
            while seen[word] > word_count[word]:
                left_word = s[left:left + word_len]
                seen[left_word] -= 1
                if seen[left_word] == 0:
                    del seen[left_word]
                left += word_len
            
            # Check if current window contains exactly what we need
            if right - left + word_len == total_words * word_len:
                result.append(left)


# DETAILED LINE-BY-LINE WALKTHROUGH WITH EXAMPLES
# Let's trace through s = "barfoothefoobarman", words = ["foo","bar"]

# STEP 1: Initial setup
# s = "barfoothefoobarman" (length 18)
# words = ["foo", "bar"]
# word_len = 3 (each word is 3 chars)
# total_words = 2 (we have 2 words)
# total_len = 6 (3 * 2 = 6 chars total for concatenation)
# word_count = {"foo": 1, "bar": 1} (frequency map)

# STEP 2: Why only check 3 starting positions?
# If word_len = 3, we only need to check positions 0, 1, 2
# Why? Because any valid match must align on word boundaries
# Position 0: check 0, 3, 6, 9, 12, 15...
# Position 1: check 1, 4, 7, 10, 13, 16...  
# Position 2: check 2, 5, 8, 11, 14, 17...

# STEP 3: Detailed trace for starting position 0
# s = "barfoothefoobarman"
#      012345678901234567
#      ^     ^     ^     ^  (positions 0, 3, 6, 9, 12, 15)

# Iteration 1: right=0, word="bar"
# - "bar" is in word_count ✓
# - seen = {"bar": 1}
# - left = 0, window size = 3, need 6 → continue

# Iteration 2: right=3, word="foo" 
# - "foo" is in word_count ✓
# - seen = {"bar": 1, "foo": 1}
# - left = 0, window size = 6, need 6 → MATCH! Add 0 to result

# Iteration 3: right=6, word="the"
# - "the" is NOT in word_count ✗
# - Reset: seen = {}, left = 9

# Iteration 4: right=9, word="foo"
# - "foo" is in word_count ✓
# - seen = {"foo": 1}
# - left = 9, window size = 3, need 6 → continue

# Iteration 5: right=12, word="bar"
# - "bar" is in word_count ✓  
# - seen = {"foo": 1, "bar": 1}
# - left = 9, window size = 6, need 6 → MATCH! Add 9 to result

# Final result: [0, 9] ✓


def test_with_detailed_trace():
    """
    Test function that shows exactly how the algorithm works
    """
    solution = Solution()
    
    # Test case 1: s = "barfoothefoobarman", words = ["foo","bar"]
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    
    print(f"Input: s = '{s}', words = {words}")
    print(f"String positions: {' '.join(f'{i:2d}' for i in range(len(s)))}")
    print(f"String chars:     {' '.join(f' {c}' for c in s)}")
    print()
    
    # Show the setup
    word_len = len(words[0])
    total_words = len(words)
    total_len = word_len * total_words
    
    print(f"word_len = {word_len}")
    print(f"total_words = {total_words}")  
    print(f"total_len = {total_len}")
    print()
    
    # Show word frequency map
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print(f"word_count = {word_count}")
    print()
    
    # Show which starting positions we'll check
    print(f"We'll check starting positions: {list(range(word_len))}")
    print()
    
    # Trace through starting position 0
    print("=== TRACING STARTING POSITION 0 ===")
    print("Checking positions: 0, 3, 6, 9, 12, 15...")
    
    for pos in range(0, len(s) - word_len + 1, word_len):
        if pos + word_len <= len(s):
            word = s[pos:pos + word_len]
            print(f"Position {pos:2d}: word = '{word}' {'✓' if word in word_count else '✗'}")
    
    print()
    result = solution.findSubstring(s, words)
    print(f"Final result: {result}")
    
    # Verify the results
    print("\n=== VERIFICATION ===")
    for start in result:
        substring = s[start:start + total_len]
        print(f"Position {start}: '{substring}' = '{s[start:start+3]}' + '{s[start+3:start+6]}'")

# Uncomment to run the trace:
# test_with_detailed_trace()
