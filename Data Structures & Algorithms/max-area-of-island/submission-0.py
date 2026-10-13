class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        visited = set()

        def dfs(l, m):
            if (l < 0 or l == len(grid) or m < 0 or m == len(grid[0]) 
                or grid[l][m] == 0
                or (l, m) in visited):
                return 0
            visited.add((l, m))
            return 1 + dfs(l + 1, m) + dfs(l - 1, m) + dfs(l, m + 1) + dfs(l, m - 1)

        for i, sublist in enumerate(grid):
            for j, item  in enumerate(sublist):
                if item == 1:
                    res = max(dfs(i, j), res)
                
        return res




        