class Solution(object):
    def countOdds(self, low, high):
        count=0
        for x in range(low,high+1):
            if(x%2 !=0):
                count+=1
        return count



"""
return (high - low) // 2 + (1 if low % 2 != 0 or high % 2 != 0 else 0)

    this also does the job pretty well and for bigger numbers
    i just wrote that first so i didn't want to change
"""