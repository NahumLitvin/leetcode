from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 1000
        max = 0
        min_candidate = 1000 #becomes the new min if we find a complemental max
        for price in prices:
            print(f'{min} , {max} , {min_candidate}')
            if price > max and price > min:
                max = price
            if price < min:
                min_candidate=price # this is the lowest price we saw
            if price - min_candidate >= max - min:
                max = price
                min = min_candidate
        return max - min
                
            
            
sol = Solution()  
print(sol.maxProfit([4,7,1,2,11]) )   