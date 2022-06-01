"""
Solution1-TC:O(1) SC:O(n)
Solution2-TC: SC:
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Solution 1
        """aset=set()
        for element in nums:
            if element in aset:
                return True
            else:
                aset.add(element)
        return False"""

        #Solution2
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                return True
            else:
                i+=1
        return False



if __name__=="__main__":
    nums = [1,2,3,1]
    a=Solution()
    k=a.containsDuplicate(nums)
    print(k)
