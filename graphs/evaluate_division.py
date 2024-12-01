# 399. Evaluate Division
# Medium
# Topics
# Companies
# Hint
# You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

# You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

# Return the answers to all queries. If a single answer cannot be determined, return -1.0.

# Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

# Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

 

# Example 1:

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0
# Example 2:

# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# Example 3:

# Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
 

# Constraints:

# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
# Seen this question in a real interview before?
# 1/5
# Yes
# No
# Accepted
# 534.2K
# Submissions
# 855.8K
# Acceptance Rate
# 62.4%

from collections import defaultdict

def calc_equation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """

    # Step 1: Build the graph
    graph = defaultdict(dict)
    
    for (dividend, divisor), value in zip(equations, values):
        graph[dividend][divisor] = value
        graph[divisor][dividend] = 1 / value
    
    # Step 2: DFS helper function
    def dfs(node, target, visited):
        if node not in graph or target not in graph:
            return -1.0
        if node == target:
            return 1.0
        
        visited.add(node)
        
        for neighbor, value in graph[node].items():
            if neighbor not in visited:
                result = dfs(neighbor, target, visited)
                if result != -1.0:  # Found a valid path
                    return result * value
        
        return -1.0  # No valid path found
    
    # Step 3: Evaluate each query
    results = []
    for dividend, divisor in queries:
        if dividend not in graph or divisor not in graph:
            results.append(-1.0)
        elif dividend == divisor:
            results.append(1.0)
        else:
            results.append(dfs(dividend, divisor, set()))
    
    return results

    
equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
print(calc_equation(equations, values, queries))



# using bfs 
from collections import defaultdict, deque

def cal_equation(equations, values, queries):
    # create an adjacent list
    adj = defaultdict(list)

    for i, eq in enumerate(equations):
        var1, var2 = eq
        adj[var1].append([var2, values[i]])
        adj[var2].append([var1, 1 / values[i]])


    # bfs of the graph
    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1

        queue_graph , visit = deque(), set()

        queue_graph.append([src, 1])

        visit.add(src)

        while queue_graph:
            node, w = queue_graph.popleft()

            if node == target:
                return w

            for nei, weight in adj[node]:
                if nei not in visit:
                    queue_graph.append([nei, w * weight])
                    visit.add(nei)


        return -1 
    
    return [bfs(src, target) for src, target in queries]

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(cal_equation(equations, values, queries))


# test case 2
equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]

values = [1.5, 2.5, 5.0]

queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
print(cal_equation(equations, values, queries)) # [3.75000, 0.40000, 5.00000, 0.20000] 
