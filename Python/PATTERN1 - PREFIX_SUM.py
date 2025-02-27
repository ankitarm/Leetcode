def prefixsum(nums):
    """
    prefix = nums[0]
    for i in range(1, len(nums)):
        prefix = prefix + nums[i]
    return prefix
    """
#Calculate in place
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
    return nums

#sum between a given range
def prefixrange(nums, l,r):
    prefix = nums[l]
    for i in range(l+1,r+1):
        prefix = prefix + nums[i]
    return prefix

nums = [3,4,5,6,2,7,1]
k = prefixsum(nums)
print(k)

'''
l = 3
r = 5
j = prefixrange(nums, l, r)
print(j)
'''