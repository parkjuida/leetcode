public class BestTimeToBuyAndSellStock {
    public int maxProfit(int[] prices) {
        int min_price = 10000;
        int answer = -1;
        for(int price: prices) {
            min_price = Math.min(price, min_price);
            answer = Math.max(price - min_price, answer);
        }
        return answer;
    }
}
