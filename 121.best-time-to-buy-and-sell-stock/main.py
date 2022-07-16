from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        max = prices[0]
        min_candidate = prices[0] #becomes the new min if we find a complemental max
        for price in prices:
            if price < min:
                min_candidate=price # this is the lowest price we saw
            if price < max and  min - min_candidate >= max-price:
                max = price
                min = min_candidate
            if price > max:
                max = price
        return max - min
                
            
            
            
            
            
# 2  5  0  4

min  2  2   
max  2  5   
cand 2  2   0