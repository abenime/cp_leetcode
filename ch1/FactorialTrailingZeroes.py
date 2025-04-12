class Solution(object):
    def trailingZeroes(self, n):
        fac=1
        count=0
        for x in range(1,n+1):
            fac*=x
        for x in str(fac)[::-1]:
            if x=="0":
                count+=1
            else:
                break
        return count