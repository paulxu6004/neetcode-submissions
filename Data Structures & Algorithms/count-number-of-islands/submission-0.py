class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        visited = set()

        def dfs(l, m, visited):
            if (l < 0 or l >= len(grid) or m < 0 or m >= len(grid[0]) #checks if outside the grid
                    or grid[l][m] == "0" # or if water
                    or (l, m) in visited): # or if already countedalready counted
                return
            visited.add((l, m))
            dfs(l, m+1, visited)
            dfs(l, m-1, visited)
            dfs(l+1, m, visited)
            dfs(l-1, m, visited)

        for i, sublist in enumerate(grid):
            for j, element in enumerate(sublist):
                if (i, j) in visited:
                    continue
                if element == "1":
                    res += 1
                    dfs(i, j, visited)

        return res
        

        