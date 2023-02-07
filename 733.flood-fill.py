# https://leetcode.com/problems/flood-fill/submissions/
from __future__ import annotations
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row_max = len(image) -1
        col_max = len(image[0]) -1
        initial_color = image[sr][sc]
        if (initial_color==color):
            return image
        image[sr][sc] = color
        if sr!=row_max and image[sr+1][sc]==initial_color:
            image = self.floodFill(image,sr+1,sc,color)
        if sc!=col_max and image[sr][sc+1]==initial_color:
            image = self.floodFill(image,sr,sc+1,color)
        if sr!=0 and image[sr-1][sc]==initial_color:
            image = self.floodFill(image,sr-1,sc,color)
        if sc!=0 and image[sr][sc-1]==initial_color:
            image = self.floodFill(image,sr,sc-1,color)
        return image

Solution().floodFill([[0,0,0],[0,0,0]],0,0,0)