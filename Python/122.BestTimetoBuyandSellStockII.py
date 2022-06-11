class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=0
        sell=1
        totalprof=0
        while sell<len(prices):  #5   <6
            diff=prices[sell]-prices[buy]   #3
            if diff>0:
                totalprof=totalprof+diff  
                #profit=diff # p=3
                buy+=1
                sell+=1
            else:
                buy+=1
                sell+=1
        return totalprof

if __name__== "__main__":
    prices = [7,1,5,3,6,4]
    #prices = [1,2,3,4,5]
    a=Solution()
    ans=a.maxProfit(prices)
    print(ans)  