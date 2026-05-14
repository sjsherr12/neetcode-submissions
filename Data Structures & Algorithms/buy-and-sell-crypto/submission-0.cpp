class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buyIndex = 0;
        int sellIndex = 0;
        int profit = 0;
        while(sellIndex < prices.size()){
            if((prices[sellIndex] - prices[buyIndex]) > profit){
                profit = prices[sellIndex] - prices[buyIndex];
            }
            if(prices[sellIndex] < prices[buyIndex]){
                buyIndex = sellIndex;
            }
            sellIndex++;
        }
        return profit;
    }
};
