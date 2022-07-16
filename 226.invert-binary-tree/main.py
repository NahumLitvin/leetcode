from functools import reduce


from typing import *
class Solution:
    def addToDict(self,s:str):
        dic: Dict[str,int]= {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        return dic
                
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1 = self.addToDict(s)
        dic2 = self.addToDict(t)
        return dic1 == dic2
            
            
sol = Solution()
sol.isAnagram("rat","cat")