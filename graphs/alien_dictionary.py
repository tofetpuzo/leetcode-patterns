# 269. Alien Dictionary
# Hard
# Topics
# Companies
# There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to you.

# You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings in words are 
# sorted lexicographically
#  by the rules of this new language.

# If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of letters, return "".

# Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there are multiple solutions, return any of them.

 

# Example 1:

# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"
# Example 2:

# Input: words = ["z","x"]
# Output: "zx"
# Example 3:

# Input: words = ["z","x","z"]
# Output: ""
# Explanation: The order is invalid, so return "".
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of only lowercase English letters.

# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 410.7K
# Submissions
# 1.1M
# Acceptance Rate
# 36.2%


def alien_order(words):
    """
    :type words: List[str]
    :rtype: str
    """
    graph = {char: [] for word in words for char in word}
    
    for word_1, word_2 in zip(words, words[1:]):
        for i in range(min(len(word_1), len(word_2))):
            if word_1[i] != word_2[i]:
                graph[word_2[i]].append(word_1[i])
                break
        else:
            if len(word_1) > len(word_2):
                return ""
            
    res = []
    white = set(graph.keys())
    black = set()
    grey = set()
    
    def dfs(node, white, black, grey, res):
        # we moving the white node to 
        
        move_node(node, white, grey)
        
        for parent in graph[node]:
            if parent in black:
                continue
            if parent in grey:
                return False
            if not dfs(parent, white, black, grey, res):
                return False
            
        move_node(node, grey, black)
        res.append(node)
        return True
        
        
    def move_node(node, current: set, target: set):
        current.discard(node)
        target.add(node)
    
    while white:
        node = next(iter(white))
        
        if not dfs(node, graph, white, black, grey, res):
            return ""
        
    return "".join(res) 
    
    
