# 1584. Min Cost to Connect All Points
# Medium
# Topics
# Companies
# Hint
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
 

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.
def minCostConnectPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    
    rows = len(points)
    cols = len(points[0])
    
    for i in range(rows):
        points[i].append(i)
        
    edges = []
    
    for i in range(rows):
        for j in range(i+1, rows):
            edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), points[i][2], points[j][2]])
            
    edges.sort()
    
    parent = [i for i in range(rows)]
    rank = [0] * rows
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        px = find(x)
        py = find(y)
        
        if px == py:
            return False
        
        if rank[px] > rank[py]:
            parent[py] = px
        elif rank[px] < rank[py]:
            parent[px] = py
        else:
            parent[px] = py
            rank[py] += 1
        
        return True
    
    res = 0
    count = 0
    
    for edge in edges:
        if union(edge[1], edge[2]):
            res += edge[0]
            count += 1
            if count == rows - 1:
                break
            
    return res
# Time complexity: O(n^2 * log(n))

# Space complexity: O(n^2)
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
print(minCostConnectPoints(points)) # 20

    
    
    
    