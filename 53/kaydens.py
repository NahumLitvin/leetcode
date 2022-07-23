from typing import List

# didn't solve this myself
# copied from having real trouble to wrap my head around this for some reason

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far= -pow(10,10)
        max_ending_here = 0
        for i in nums:
            max_ending_here+=i
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
            if max_ending_here<0:
                max_ending_here=0
        return max_so_far

        
    
print(Solution().maxSubArray([4,1,3])==8)
print(Solution().maxSubArray([-4,1,3])==4)
print(Solution().maxSubArray([4,-1,3])==6)
print(Solution().maxSubArray([4,-8,3])==4)
print(Solution().maxSubArray([3,-8,4])==4)
print(Solution().maxSubArray([-3,-8,-4])==-3)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000])==-10000)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000]))