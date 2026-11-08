// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Difficulty: Easy | Topic: Arrays

#include <bits/stdc++.h>
using namespace std;

// Write your solution below this line.

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int buy = prices[0];
        int profit = 0;
        for (int i = 1; i < prices.size(); i++) {
            if (prices[i] < buy) {
                buy = prices[i];
            } else if (prices[i] - buy > profit) {
                profit = prices[i] - buy;
            }
        }
        return profit;
    }
};

/*
Explanation:
  To get the most profit from selling on day i, buy at the lowest price
  before day i. So walk through the prices once and keep two values:
    - buy:    the lowest price seen so far (the best day to have bought)
    - profit: the best profit seen so far
  On each day:
    - If today's price is lower than buy, it is a better buying day. Update
      buy. Selling today cannot beat the current profit, because selling on
      the day you buy makes 0.
    - Otherwise, try selling today at prices[i] - buy, and keep it if it
      beats the current profit.
  profit starts at 0, so if prices only fall, the answer is 0 (no trade).

Complexity:
  Time:  O(n), one pass over the prices
  Space: O(1), two variables

Dry run:
  prices = [7, 1, 5, 3, 6, 4]
  start: buy = 7, profit = 0

  i | prices[i] | action                     | buy | profit
  --+-----------+----------------------------+-----+-------
  1 |     1     | 1 < 7, new lowest price    |  1  |   0
  2 |     5     | 5 - 1 = 4 > 0, new best    |  1  |   4
  3 |     3     | 3 - 1 = 2, not > 4         |  1  |   4
  4 |     6     | 6 - 1 = 5 > 4, new best    |  1  |   5
  5 |     4     | 4 - 1 = 3, not > 5         |  1  |   5

  Answer: 5 (buy on day 1 at price 1, sell on day 4 at price 6)

  prices = [7, 6, 4, 3, 1]: every price is a new lowest, so profit stays 0.

Note:
  The solution is my own. I used AI to help write this explanation, so my
  ideas are explained in a clear, standard way that anyone can follow.
*/
