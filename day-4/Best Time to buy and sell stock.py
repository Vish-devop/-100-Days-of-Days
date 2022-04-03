'''
121. Best Time to Buy and Sell Stock
Easy #leetcode

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

'''
    My Algo: 
    1. Intialized left and right and max_profit as 0,1,0
    2. Now, in a while loop I am checking if my right < length of prices:
    3. Then,if the condition is satisfied, then I am going find my current profit as prices[right]-prices[left]
    4. Again, I'll check the condition that if prices[left]<prices[right] then,
    5. max_profit = max(curr_profit,max_profit)
    5. If the condition got failed, in that scenario my left pointer = right pointer.
    and at end right will be incremented.
    6. At last return the max_profit.
'''
def BestTimeToBuyAndSellStock(prices):
    left=0
    right=1
    max_profit=0
    while right<len(prices):
        curr_profit=prices[right]-prices[left]
        if prices[left]<prices[right]:
            max_profit=max(curr_profit,max_profit)
        else:
            left=right
        right+=1
    return max_profit

#driver code
prices=[7,1,5,3,6,4]
print(BestTimeToBuyAndSellStock(prices))