
# Problem Number 9

class Solution:
    def isPalindrome(self, x: int) -> bool:
        cstring = str(x)
        s = cstring[::-1]
        if (s==cstring):
            return True
        else:
            return False