class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        least,result = float('inf'),0
        for index,value in enumerate(nums):
            left, right=index+1,len(nums)-1
            while left<right:
                tot=value+nums[left]+nums[right] #-3
                if tot<target: #-3<1
                    left+=1  #2
                elif tot>target:
                 right-=1
                else:
                    return target
                diff=abs(tot-target) #-3-1=4
                if diff<least:
                    least=diff
                    result=tot
        return result

if __name__=="__main__":
    a=Solution()
    nums=[1,1,1,0]
    #nums=[-1,2,1,-4]
    target=-100
    tot=a.threeSumClosest(nums,target)
    print(tot)