class Solution(object):
    def function(self, nums, target) :
        """a=[]
        for i in range(-target,len(nums)-target):
            a.append(nums[i])
        return a"""

        #return([nums[i] for i in range(-target,len(nums)-target)])
        """for i in range(target):  #O(n*n)
            target%=len(nums)
            k=nums.pop()
            o=nums.insert(0,k)
            print(nums)"""
        k=len(nums)
        target%=len(nums) #5%2=2
        nums[:]=nums[len(nums)-target:]+nums[:len(nums)-target]
        print(nums)




if __name__=="__main__":
    a=Solution()
    #nums=[0,1,3,5,2]
    #nums=[-1,-100,3,99]
    #nums=[1,2,3,4,5,6,7]
    nums=[1,2]
    target=5
    tot=a.function(nums,target)
    #print(tot)