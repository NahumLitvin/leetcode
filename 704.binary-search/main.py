#https://leetcode.com/problems/binary-search/
from operator import truediv
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        middle = -1
        while right-left > 1:
            middle = left + (((right - left) // 2))       
            print(f"{left}, {right} , {middle}")      
            if nums[middle] == target: # middle is correct we are done
                return middle
            if nums[middle] < target: # middle is smaller then target search right
                left = middle
            if nums[middle] > target: # middle is bigger then target search left
                right = middle    
        if nums[left] == target:
            return right
        if nums[right] == target:
            return right
        return -1
            
                
            
sol = Solution()
# print(sol.search([-1,0,3,5,9,12], -1))
# print(sol.search([-1,0,3,5,9,12], 0))
# print(sol.search([-1,0,3,5,9,12], 3))
# print(sol.search([-1,0,3,5,9,12], 5))
# print(sol.search([-1,0,3,5,9,12], 9))
print(sol.search([-1,0,3,5,9,12], 2))
