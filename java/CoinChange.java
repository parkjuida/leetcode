import java.util.Arrays;
import java.util.HashMap;

public class CoinChange {
    private int[] amountHistory = new int[10000];

    public int find(int[] coins, int amount) {
        if(amount < 0) return -1;
        if(amountHistory[amount] > -2) return amountHistory[amount];
        if(amount == 0) return 0;

        for(int i = coins.length - 1; i >= 0; i--) {
            int result = find(coins, amount - coins[i]);

            if(result != -1) {
                if(amountHistory[amount] == -2) {
                    amountHistory[amount] = result + 1;
                } else {
                    amountHistory[amount] = Math.min(result + 1, amountHistory[amount]);
                }
            }
        }

        if(amountHistory[amount] == -2) {
            amountHistory[amount] = -1;
        }
        return amountHistory[amount];
    }

    public int coinChange(int[] coins, int amount) {
        Arrays.fill(amountHistory, -2);
        return find(coins, amount);
    }

    public static void main(String[] args) {
        CoinChange coinChange = new CoinChange();
        int result = coinChange.coinChange(new int[]{1, 2, 5}, 11);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{2}, 3);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{1}, 0);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{1}, 1);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{1}, 2);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{2, 3}, 6);
        System.out.println(result);
        result = coinChange.coinChange(new int[]{186, 419, 83, 408}, 6249);
        System.out.println(result);
    }
}
