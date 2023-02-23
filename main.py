# shoutout 3blue1brown fr
# https://www.youtube.com/watch?v=KuXjwB4LzSA

import cv2

img = cv2.imread('src/mario.png', 1)
length = int(img[0].size/3)
width = int(img.size/length/3)

grid = [[1/16, 1/8, 1/16], [1/8, 1/4, 1/8], [1/16, 1/8, 1/16]]
glength = len(grid[0])
print(glength)
gwidth = len(grid)
print(gwidth)
glbuffer = int((glength-1)/2)
gwbuffer = int((gwidth-1)/2)

bordered = cv2.copyMakeBorder(src=img, top=glbuffer, bottom=glbuffer, left=gwbuffer, right=gwbuffer, borderType=cv2.BORDER_REFLECT) 

cv2.imshow(':3', bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(glbuffer, length-1):
    for j in range(gwbuffer, width-1):
        red = 0
        blue = 0
        green = 0
        for x in range(3):
            for y in range(3):
                red += img[i+(x-1)][j+(y-1)][0] * grid[x][y]
                green += img[i+(x-1)][j+(y-1)][1] * grid[x][y]
                blue += img[i+(x-1)][j+(y-1)][2] * grid[x][y]
        bordered[i][j] = [red, green, blue]

cv2.imshow(':3', bordered)
cv2.waitKey(0)
cv2.destroyAllWindows()