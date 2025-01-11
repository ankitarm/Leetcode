class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        '''k=[]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                k.append(True)
            else:
                k.append(False)
        return k'''
        return [candies[i] + extraCandies >= max(candies) for i in range(len(candies))]

if __name__ == "__main__":
    candies=[2,3,5,1,3]
    extraCandies=3
    a=Solution()
    k=a.kidsWithCandies(candies, extraCandies)
    print(k)
    