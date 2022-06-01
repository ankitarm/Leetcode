# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
"""
TC: O(logn)
"""

def isBadVersion(mid):
    if mid ==2 or mid== 3 or mid== 4 or mid==5:
        return True
    elif  mid == 1:
        return False
    else:
        return False


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low <= high:  # 0<5
            mid = (high + low) // 2  # 4
            ans = isBadVersion(mid)
            if ans:
                result=mid
                high = mid - 1
            else:
                low = mid + 1
        return result

if __name__=="__main__":
    n = 5
    bad = 4
    a=Solution()
    k=a.firstBadVersion(n)
    print(k)