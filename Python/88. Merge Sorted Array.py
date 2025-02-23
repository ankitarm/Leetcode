'''
Time Complexity: O(m+n), since we traverse both arrays once.
Space Complexity: O(1), as we modify nums1 in-place.

'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        endnum1, endnum2, endmerge = m-1, n-1, m+n-1
        while endnum2 >= 0:
            if nums1[endnum1] > nums2[endnum2] and endnum1 >= 0:
                nums1[endmerge] = nums1[endnum1]
                endnum1-=1
            else:
                nums1[endmerge] = nums2[endnum2]
                endnum2 -= 1
            endmerge-=1
        return nums1

if __name__=="__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    a=Solution()
    k=a.merge(nums1, m, nums2, n)
    print(k)