# 2876. Count Visited Nodes in a Directed Graph
# Hard
# Topics
# Companies
# Hint
# There is a directed graph consisting of n nodes numbered from 0 to n - 1 and n directed edges.

# You are given a 0-indexed array edges where edges[i] indicates that there is an edge from node i to node edges[i].

# Consider the following process on the graph:

# You start from a node x and keep visiting other nodes through edges until you reach a node that you have already visited before on this same process.
# Return an array answer where answer[i] is the number of different nodes that you will visit if you perform the process starting from node i.


# Example 1:


# Input: edges = [1,2,0,0]
# Output: [3,3,3,4]
# Explanation: We perform the process starting from each node in the following way:
# - Starting from node 0, we visit the nodes 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 3.
# - Starting from node 1, we visit the nodes 1 -> 2 -> 0 -> 1. The number of different nodes we visit is 3.
# - Starting from node 2, we visit the nodes 2 -> 0 -> 1 -> 2. The number of different nodes we visit is 3.
# - Starting from node 3, we visit the nodes 3 -> 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 4.
# Example 2:


# Input: edges = [1,2,3,4,0]
# Output: [5,5,5,5,5]
# Explanation: Starting from any node we can visit every node in the graph in the process.


# Constraints:

# n == edges.length
# 2 <= n <= 105
# 0 <= edges[i] <= n - 1
# edges[i] != i


class Solution(object):
    def countVisitedNodes(self, edges):
        """
        :type edges: List[int]
        :rtype: List[int]
        """
        num_cities = len(edges)  # Total number of cities
        answer = [
            0
        ] * num_cities  # Initialize array to store answer for each starting city

        for start_city in range(num_cities):  # Try every city as start point
            visited_cities = set()  # Cities visited during this specific trip
            current_city = start_city
            trip_count = 0  # Number of cities visited on the current trip

            while (
                current_city not in visited_cities
            ):  # Keep going until we hit a city we've already visited
                visited_cities.add(current_city)
                trip_count += 1
                current_city = edges[current_city]  # Travel down the road to next city

            # We have detected a cycle in the current trip.
            # store the number of distinct visited cities from this trip.
            answer[start_city] = trip_count

        return answer


# class Solution(object):
#     def countVisitedNodes(self, edges):
#         """
#         :type edges: List[int]
#         :rtype: List[int]
#         """
#         N = len(edges)
#         ans = [None] * N
#         INF = 10**20
#         visited = [INF] * N

#         t = 0
#         until = None
#         found = False

#         def go(node):
#             nonlocal t
#             visited[node] = t
#             t += 1
#             nonlocal until

#             if visited[node] == float("inf"):
#                 go(edges[node])
#                 if node == until:
#                     nonlocal found
#                     found = True
#                     ans[node] = ans[edges[node]]
#                 elif found or (until is None):
#                     ans[node] = ans[edges[node]] + 1
#                 else:
#                     ans[node] = ans[edges[node]]

#             else:
#                 if ans[edges[node]] is not None:
#                     ans[node] = ans[edges[node]] + 1
#                 else:
#                     ans[node] = visited[node] - visited[edges[node]]

#                     until = edges[node]

#         for i in range(N):
#             if visited[i] == float("inf"):
#                 t = 0
#                 until = None
#                 found = False
#                 go(i)
#         return ans
