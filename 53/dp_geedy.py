from typing import List

# didn't solve this myself
# copied from having real trouble to wrap my head around this for some reason

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far= nums[0]
        curr_max = nums[0]
        for i in nums[1:]:
            curr_max= max(i,curr_max+i) # if new i positive add it to curr
            max_so_far=max(curr_max,max_so_far)# if its bigger then last ma set as new max
        return max_so_far

        
    
print(Solution().maxSubArray([4,1,3])==8)
print(Solution().maxSubArray([4,-99,1,1,1,1,1])==5)
print(Solution().maxSubArray([-4,1,3])==4)
print(Solution().maxSubArray([4,-1,3])==6)
print(Solution().maxSubArray([4,-8,3])==4)
print(Solution().maxSubArray([3,-8,4])==4)
print(Solution().maxSubArray([-3,-8,-4])==-3)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000])==-10000)
print(Solution().maxSubArray([-10000,-10000,-10000,-10000]))