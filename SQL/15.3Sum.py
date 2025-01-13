"""import numpy as np


class Solution(object):
    def threeSum(self, nums):

        if len(nums) == 0:
            return nums
        elif len(nums) == 1 and nums[0] == 0:
            return []
        else:
            assorted = []
            assorted = sorted(nums)
            print(assorted)
            lista = []

            for index, value in enumerate(assorted):  # 1,-1

                left = index + 1  # 2
                right = len(assorted) - 1  # 5
                while (left < right):  # 3<4
                    s = assorted[left] + assorted[right]  # 0+1=1
                    totsum = s + value  # 1+(-1)=0
                    if totsum == 0:
                        lista.append([value, assorted[left], assorted[right]])
                        left += 1
                        right -= 1
                        continue
                    elif totsum > 0:
                        right -= 1  #
                    else:
                        left += 1  # 5

            #print(list(dict.fromkeys(lista)))
            #return list(set(tuple(lista)))
            return [list(t) for t in set(tuple(i) for i in lista)]


if __name__== "__main__":
    nums=[-1,0,1,2,-1,-4]
    #nums=[0]
    a=Solution()
    ans=a.threeSum(nums)
    #set(ans)
    print(ans)
    #print(np.array(ans))"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lista, tot = [], 0
        nums.sort()
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while (left < right):
                tot = value + nums[left] + nums[right]
                if tot == 0:
                    lista.append([value, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif tot < 0:
                    left += 1
                else:
                    right -= 1
        return lista

if __name__== "__main__":
    nums=[-1,0,1,2,-1,-4]
    #nums=[0,0,0]
    #nums=[-2,0,0,2,2]
    a=Solution()
    ans=a.threeSum(nums)
    #set(ans)
    print(ans)