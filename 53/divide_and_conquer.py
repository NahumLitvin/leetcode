from re import S
from typing import List

# didn't solve this myself
# copied from having real trouble to wrap my head around this for some reason

class Solution:
    def daq(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            arr =  [nums[0]] * 4
            return arr
        mid = len(nums) // 2
        # s = sum of all array items
        # l = sum of all array items to the left of mid
        # r = sum of all array items to the rigt of mid
        # m = sum of maxSubArray items
        ls,ll,lr,lm = self.daq(nums[:mid])
        rs,rl,rr,rm = self.daq(nums[mid:])
        
        s = ls + rs
        l = max(ll,ls,ls+rl,s)
        r = max(rr,rs,rs+lr,s)
        m = max(lm,rm,s,lr + rl,l,r)
        return s,l,r,m
    def maxSubArray(self, nums: List[int]) -> int:
        _,_,_,m = self.daq(nums)
        return m


        

        
    
print(Solution().maxSubArray([4,1,3])==8)
print(Solution().maxSubArray([4,-99,1,1,1,1,1])==5)
print(Solution().maxSubArray([-4,1,3])==4)
print(Solution().maxSubArray([4,-1,3])==6)
print(Solution().maxSubArray([4,-8,3])==4)
print(Solution().maxSubArray([3,-8,4])==4)
print(Solution().maxSubArray([-3,-8,-4])==-3)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000])==-10000)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000]))