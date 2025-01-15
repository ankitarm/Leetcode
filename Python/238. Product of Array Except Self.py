class Solution(object):
    def productExceptSelf(self, nums):
        result = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix = prefix*nums[i]
        suffix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]= suffix*result[i]
            suffix = suffix *nums[i]
        return result



'''   def productarray(self, nums):
        result=[]
        for i in range(len(nums)):
            sum1 = 1
            for j in range(len(nums)):
                if j!=i:
                    sum1=sum1*nums[j]
            #result.append(sum1)
            nums[i]=sum1
        return nums'''

if __name__=="__main__":
    nums=[1,2,3,4]
    a= Solution()
    k=a.productExceptSelf(nums)
    print(k)