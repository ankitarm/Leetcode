class Solution(object):
    def mostwater(self,height):
        n = len(height)
        left = 0
        right = n-1
        maxarea = float('-inf')
        while left < right:
            area = min(height[left] , height[right])*(right-left)
            if area > maxarea:
                maxarea = area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea
        #[1, 8, 6, 2, 5, 4, 8, 3, 7]


if __name__ == "__main__":
    #height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    height = [1, 1]
    a = Solution()
    k = a.mostwater(height)
    print(k)