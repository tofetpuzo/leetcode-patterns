# 1. Initialization: search_history = SearchHistory()

# A new SearchHistory object is created.

# It initializes an empty Trie with a root node ( self.root is a TrieNode ). The root node initially has an empty children dictionary and an empty frequencies dictionary.

# 2. First Search: search_history.search("apple", 3)

# update_frequency("apple"):

# It starts at the root node.

# 'a': Checks if 'a' exists as a child of the root. It doesn't, so a new TrieNode is created for 'a' and added as a child in the root node's children. The frequencies dictionary for this new node is {"apple": 1}. Now the current node becomes the child node 'a'.

# 'p': Checks if 'p' exists as a child. It doesn't, so create a new node, add 'p' to the child of 'a'. The frequencies dictionary is now {"apple": 1}. Current node is now node 'p'.

# 'p': Similarly, creates a node for the second 'p', the frequencies dictionary is now {"apple": 1}. Current node is now the second node 'p'.

# 'l': A new node is created and added as a child of 'p', the frequencies dictionary is now {"apple": 1}. Current node is now 'l'.

# 'e': A new node is created and added as a child of 'l', the frequencies dictionary is now {"apple": 1}. Current node is now 'e'. The flag is_end_of_word is set to True.

# get_top_k_matches("apple", 3):
# - It traverses down the tree to reach the end of the word "apple" following the same steps above to the node 'e'.
# - The frequencies map of node 'e' is {"apple":1}.
# - A min heap is created to keep track of the frequency of this map. In this case heap = [(-1, "apple")]
# - Pop the top k elements from heap.
# - It returns ["apple"]

# 3. Second Search: search_history.search("app", 3)

# update_frequency("app"):

# Starts at the root.

# 'a': Node 'a' already exists, so it moves to node 'a'. The frequencies map of node 'a' is now {"apple":1, "app":1}

# 'p': Node 'p' under node 'a' already exists, so it moves to the node 'p'. The frequencies map of this 'p' node is now {"apple":1, "app":1}

# 'p': Node 'p' under second 'p' node already exists, so it moves to the node 'p'. The frequencies map of this node is now {"apple":1, "app":1}. The is_end_of_word flag is set to True.

# get_top_k_matches("app", 3):
# - It traverses to the end of the word "app".

# The frequencies map of the node 'p' is {"apple":1, "app":1}
# - A min heap is created: [(-1, "apple"), (-1, "app")]
# - Pop the top 2 elements of heap: Returns ["apple","app"]

# 4. Third Search: search_history.search("application", 3)

# update_frequency("application"):

# Similar to before, it traverses down the Trie, creating new nodes if they don't exist.

# Updates the frequencies maps at nodes a, p, p, l (from apple), i, c, a, t, i, o, n to {"apple":1,"app":1,"application":1} at all the nodes that exist, and {"application":1} for new nodes.

# get_top_k_matches("application", 3):
# - It returns ["application"].

# 5. Fourth Search: search_history.search("apricot", 3)

# update_frequency("apricot"):

# Similar to before, it traverses down the Trie, creating new nodes if they don't exist.

# Updates the frequencies maps at nodes a, p, to {"apple":1,"app":1,"application":1, "apricot":1} and all new nodes to {"apricot":1}

# get_top_k_matches("apricot", 3):

# It returns ["apricot"].

# 6. Fifth Search: search_history.search("banana", 3)

# update_frequency("banana"):

# Similar to before, it traverses down the Trie, creating new nodes if they don't exist.

# frequencies is updated as per terms

# get_top_k_matches("banana", 3):

# It returns ["banana"].

# 7. Sixth and Seventh Search: search_history.search("app", 3) two times

# - Same process as step 3, updates the frequency of `app` across all prefix nodes
# -The frequencies at node 'p' is now: `{"apple":1, "app":3, "application":1,"apricot":1}`
# Use code with caution.
# 8. Subsequent Searches (Example with "app", "a", "b", "ap"):

# search_history.search("app", 3):

# Traverses to node p at end of app.

# Gets frequencies at node p: {"apple":1, "app":3, "application":1, "apricot":1}.

# Heapifies: [(-3, "app"), (-1, "apple"), (-1, "application"), (-1, "apricot")]

# Returns top 3: ['app', 'application', 'apple']

# search_history.search("a", 3):

# Traverses to node a.

# Gets frequencies at node a: {"apple":1, "app":3, "application":1, "apricot":1}

# Heapifies: [(-3, "app"), (-1, "apple"), (-1, "application"), (-1, "apricot")]

# Returns top 3: ['app', 'apple', 'application']

# search_history.search("b", 2):

# Traverses to node b.

# Gets frequencies at node b: {"banana":1}

# Heapifies: [(-1, "banana")]

# Returns top 2: ['banana']

# search_history.search("ap", 2):

# Traverses to node p.

# Gets frequencies at node p: {"apple":1, "app":3, "application":1,"apricot":1}

# Heapifies: [(-3,"app"), (-1, "apple"),(-1,"application"), (-1, "apricot")]

# Returns top 2: ['app', 'apple']

# - **`search_history.search("ap", 3)`:**
#    - Traverses to node `p`.
#    - Gets frequencies at node `p`: `{"apple":1, "app":3, "application":1,"apricot":1}`
#    - Heapifies: `[(-3,"app"), (-1, "apple"),(-1,"application"), (-1, "apricot")]`
#    - Returns top 3: `['app', 'apple', 'apricot']`
# Use code with caution.
# Key Observations:

# Prefix Sharing: The Trie structure allows efficient prefix lookups. We can quickly find the node corresponding to a given prefix.

# Frequency Map: The frequency map at each node makes it very fast to find the most frequent terms with a given prefix.

# Heap: The heap efficiently retrieves the top k elements based on frequency.

# Let me know if you'd like to explore any part of this  further!

import heapq
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = {}  # Maps character to TrieNode
        self.frequencies = defaultdict(int)  # Maps search term to frequency
        self.is_end_of_word = False


class SearchHistory:
    def __init__(self):
        self.root = TrieNode()

    def update_frequency(self, term):
        """
        Updates the frequency of a search term in the Trie.
        """
        node = self.root
        for char in term:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.frequencies[
                term
            ] += 1  # Update the frequency of this term in all prefixes
        node.is_end_of_word = True

    def get_top_k_matches(self, search_input, k):
        """
        Returns the top K most frequent search terms with the given prefix.
        """
        node = self.root
        for char in search_input:
            if char not in node.children:
                return []  # No matching prefixes
            node = node.children[char]

        # Use a min heap to get top k frequent items
        heap = [(-freq, term) for term, freq in node.frequencies.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(min(k, len(heap))):  # return min of k or number of matched terms
            neg_freq, term = heapq.heappop(heap)
            result.append(term)
        return result

    def search(self, search_input, k):
        """
        Updates the search term frequency and then get top k matching terms
        """
        self.update_frequency(search_input)
        return self.get_top_k_matches(search_input, k)


# Example Usage
search_history = SearchHistory()

# Initial Search terms:
search_history.search("apple", 3)
search_history.search("app", 3)
search_history.search("application", 3)
search_history.search("apricot", 3)
search_history.search("banana", 3)
search_history.search("app", 3)
search_history.search("app", 3)

print(search_history.search("app", 3))  # Output: ['app', 'application', 'apple']
print(search_history.search("a", 3))  # output ['app', 'apple', 'application']
print(search_history.search("b", 2))  # output ['banana']
print(search_history.search("ap", 2))  # output: ['app', 'apple']
print(search_history.search("ap", 3))  # output: ['app', 'apple', 'apricot']
