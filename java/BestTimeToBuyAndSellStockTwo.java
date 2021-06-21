public class BestTimeToBuyAndSellStockTwo {

    public int maxProfit(int[] prices) {
        int min_price = 10000;
        int answer = 0;
        for(int price: prices) {
            min_price = Math.min(price, min_price);
            answer += price - min_price;
            if (price - min_price > 0) {
                min_price = price;
            }
        }

        return answer;
    }
}
