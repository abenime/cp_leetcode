class Solution(object):
    def intersect(self, nums1, nums2):
        # z=[]
        # for x in nums1:
        #     if (x in nums1) and (x in nums2):
        #         z.append(x)
        # return z
        
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        return result