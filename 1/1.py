from typing import *


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes_of_keys_in_list : Dict = {}
        for i in range(len(nums)):
            key = nums[i]
            indexes_of_keys_in_list[key] = i
            pair_value = target - key
            if pair_value in indexes_of_keys_in_list:
                return [i , indexes_of_keys_in_list[pair_value]]
        
sol =  Solution()
print(sol.twoSum([2,7,11,15], 9))