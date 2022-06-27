class Solution(object):
  def maxArea(self, height):
    
    #Brute Force
    #TC=O(n*n)
    """     areamax=0
        for ltht in range(len(height)):   0:9
            for rtht in range(ltht+1,len(height)):  2:9
                breadth=min(height[ltht],height[rtht])  1
                length=rtht-ltht   2
                areaw=breadth*height 2
                areamax=max(areaw,areamax) 2
            return areamax
"""

    """TC:O(n)"""
    areamax=0
    ltht,rtht=0,len(height)-1
    while ltht<rtht:
        length=rtht-ltht
        breadth=min(height[ltht],height[rtht])
        areaw=breadth*length
        areamax=max(areaw,areamax)
        if height[ltht]<height[rtht]:
            ltht+=1
        else:
            rtht-=1
    return areamax



if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    a=Solution()
    i=a.maxArea(height)
    print(i)