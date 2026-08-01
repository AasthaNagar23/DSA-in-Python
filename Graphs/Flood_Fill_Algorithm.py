# Flood Fill Algorithm
def dfs(image,r,c,old_color,new_color):
    if r<0  or c<0 or r>=len(image) or c>=len(image[0]):
        return
    if image[r][c]!=old_color:
        return 
    image[r][c]=new_color
    dfs(image,r-1,c,old_color,new_color)
    dfs(image,r+1,c,old_color,new_color)
    dfs(image,r,c-1,old_color,new_color)
    dfs(image,r,c+1,old_color,new_color)
def flood_fill(image,sr,sc,color): # color here is the new color we are going to fill
    old_color=image[sr][sc]
    if old_color==color:
        return image
    dfs(image,sr,sc,old_color,color)
    return image
image = [
[1,1,1],
[1,1,0],
[1,0,1]
]

print(flood_fill(image,1,1,2))