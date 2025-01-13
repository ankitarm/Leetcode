
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxPro = 0
        buy = 0  #7
        sell = 1 #1
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maxPro = max(profit,maxPro)
            else:
                buy = buy+1
            sell = sell+1
        return maxPro

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    a = Solution()
    i=a.maxProfit(prices)
    print(i)
