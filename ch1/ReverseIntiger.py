class Solution(object):
    def reverse(self, x):
        stg=""
        num=0
        if (x < 0):
            for y in range(1,len(str(x))):
                stg+=str(x)[y]
            num=int(stg[::-1])
            num*=-1
        elif x >0:
            stg=str(x)[::-1]
            num=int(stg)
        else:
            num=0
        
        if(num<(-2**31)) or (num>(2**31)-1):
            return 0
        else:
            return num