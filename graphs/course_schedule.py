# 207. Course Schedule
# Medium
# Topics
# Companies
# Hint
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.


# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


# Constraints:

# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


# Time complexity: O(V+E)
# Space complexity: O(V+E)

# Approach 2: DFS


def can_finish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    graph = {}
    for i in range(numCourses):
        graph[i] = []
    for course, pre in prerequisites:
        graph[pre].append(course)
    visited = [0] * numCourses

    def dfs(node):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        visited[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True


# Time complexity: O(V+E)
# Space complexity: O(V+E)

# test case
numCourses = 2
prerequisites = [[1, 0]]
print(can_finish(numCourses, prerequisites))


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(can_finish(numCourses, prerequisites))


numCourses = 3
prerequisites = [[1, 0], [2, 1]]
print(can_finish(numCourses, prerequisites))
