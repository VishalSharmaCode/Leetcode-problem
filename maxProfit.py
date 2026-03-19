class Solution:
    def maxProfit(prices):
        if not prices:
            return 0
        
        buy1 = float('inf')
        sell1 = 0
        buy2 = float('inf')
        sell2 = 0
        
        for price in prices:
            # First transaction: standard "Buy Low, Sell High"
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            
            # Second transaction: Reinvest the profit from sell1
            # buy2 is the 'effective' price of the second stock
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)
            
        return sell2