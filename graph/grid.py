from collections import deque

class Grid:
    def __init__(self, grid:list[list[int]]):
        self.grid:list[list[int]] = grid
        self.rows:int = len(grid)
        self.cols:int = len(grid[0]) if self.rows > 0 else 0
    
    def print_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print (self.grid[i][j], end=" ")
            print()

    def num_islands_dfs(self) -> int:
        visited = set()
    
        def dfs(r,c):
            if  r < 0 or c < 0 or \
                r >= self.rows or c>= self.cols or \
                (r,c) in visited or self.grid[r][c] == 0:
                return
            visited.add((r,c))
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r+1,c)

        count = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) not in visited:
                    if self.grid[r][c] == 1:
                        count += 1
                        dfs(r,c)
        return count

    def num_islands_bfs(self) -> int:
        visited = set()

        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))

            while q:
                x,y = q.popleft()
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx = x+dx
                    ny = y+dy

                    if nx < 0 or nx >= self.rows or \
                        ny < 0 or ny >= self.cols or \
                        (nx,ny) in visited or self.grid[nx][ny] == 0:
                        continue

                    visited.add((nx,ny))
                    q.append((nx,ny))

        count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if (r,c) not in visited:
                    if self.grid[r][c] == 1:
                        count += 1
                        bfs(r,c)
        return count

grid = Grid([[1,0,1,0,1],
             [0,1,0,1,0],
             [1,0,1,0,1],
             [0,1,0,1,0],
             [1,1,0,1,0]])

grid.print_grid()
print(grid.num_islands_dfs())
print(grid.num_islands_bfs())