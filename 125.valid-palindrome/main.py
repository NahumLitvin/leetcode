class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j = len(s) -1
        while i<j:
            print(f"{i},{j},{s[i]},{s[j]}")
            if not s[i].isalnum():
                i+=1
                continue
            if not s[j].isalnum():
                j-=1
                continue
            if s[i].lower() == s[j].lower():
                i+=1
                j-=1
                continue
            return False
        return True

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))
    
    #"A man, a plan, a canal: Panama"
    #Aa
    # m
    #mm
    #aa
    #nn
    #,a
    # a
    #aa
    # P
    #pP
    #l 
    #l:
    #ll
    #aa
    #nn
    #,a
    # a
    #aa
    #cc
    
    
    #a ca
    # c
    
    
    #bbb
    #b@b
    #@x@BB@

            