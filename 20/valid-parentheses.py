from collections import deque
from site import PREFIXES
from sys import prefix

class Solution:
    PREFIXES = ['{','[','(']
    SUFFIXES = ['}',']',')']
    PAIRS = {'{':'}',
             '[':']',
             '(':')'}
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in s:
            if i in self.PREFIXES:
                stack.append(i)
            elif i in self.SUFFIXES:
                res = stack.pop() if stack else None
                if not res or i != self.PAIRS[res]:
                    return False
            else:# not valid
                return False
        return len(stack) == 0





s = Solution()

print(False == s.isValid("ads"))
print(False == s.isValid("("))
print(False == s.isValid("({)"))
print(False == s.isValid("]"))
print(True == s.isValid("()"))
print(True == s.isValid("({})"))