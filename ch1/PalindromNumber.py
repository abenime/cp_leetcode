class Solution(object):
    def isPalindrome(self, x):
        valid= False
        y=str(x)[::-1]
        if y==str(x):
            valid =True
        return valid
    