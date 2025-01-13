import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffdict={} #time complexity for searching a key in dictionnary is O(1) and so avoiding array in place to store
        for index, value in enumerate(nums): #2,5
            if value in diffdict:
                return diffdict[value],index  #(2,)
            diff=target-value  #9-4=5
            diffdict[diff]=index # {7:0,5:1,   }
            #print(diffdict)





if __name__ == "__main__":
    #nums = [2, 4, 5, 0,7,9,11]
    nums=[3,3]
   # nums=[2,7,11,15]
    target = 6
    a=Solution()
    i=a.twoSum(nums,target)
    print(np.array(i))




