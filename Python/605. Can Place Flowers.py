class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                print(i)
                # check if left and right are empty
                leftempytplot = i == 0 or flowerbed[i - 1] == 0  # i==0 1st plot
                rightemptyplot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)  # last plot or right
                # next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                if leftempytplot and rightemptyplot:
                    flowerbed[i] = 1
                    count += 1
                    print(f"count:{count}")
                    if count == n: #to end if count is already found
                        print(count)
                        return True

        return count >= n

if __name__=="__main__":
    flowerbed = [1,0,0,0,0,0,0,0,1]
    n = 1
    a=Solution()
    k=a.canPlaceFlowers(flowerbed,n)
    print(k)