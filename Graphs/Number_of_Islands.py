def dfs(grid,r,c):
    if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]):  #greater than equal lagana mat bhulna also grid[0] bhi
        return
    if grid[r][c]=="0":
        return
    grid[r][c] = '0'  #agar nahi then means agar 1 hua then use 0 bna diya he 
    dfs(grid,r-1,c)
    dfs(grid,r+1,c)
    dfs(grid,r,c-1)
    dfs(grid,r,c+1)
def number_of_island(grid):
    count=0
    for i in range(len(grid)):
        for j in range(len(grid[0])): #1st row ka length
            if grid[i][j]=="1":
                count+=1
                dfs(grid,i,j)
    return count
grid = [
['1','1','0','0'],
['1','0','0','1'],
['0','0','1','1'],
['0','0','0','0']
]

print(number_of_island(grid))
        
