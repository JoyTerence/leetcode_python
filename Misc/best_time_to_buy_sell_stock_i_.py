
def best_time_to_buy_sell_stock(prices):

    max_profit, diff = 0, 0

    for i in range(len(prices)-1):
        diff += prices[i+1] - prices[i]
        diff = max(diff, 0)
        max_profit = max(max_profit, diff)
    
    return max_profit

'''
Time: O(N)
Space: O(1)
'''
