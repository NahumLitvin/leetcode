from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        min_candidate = prices[0] #becomes the new min if we find a complemental max
        for price in prices:
            if price < min and price < max and price < min_candidate:
                min_candidate=price # this is the lowest price we saw
            if price - min_candidate >= max - min:
                max = price
                min = min_candidate
        return max - min
                
            
            
sol = Solution()  
print(sol.maxProfit([4,7,1,2,11]) )   