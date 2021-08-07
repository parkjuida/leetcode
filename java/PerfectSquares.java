import java.util.Arrays;

public class PerfectSquares {
    public int calcSquares(int n, int[] history) {
        if(history[n] != -1) {
            return history[n];
        }
        int operand = (int) Math.sqrt((double)n);
        int ret = 1000;
        for(int i = operand; i > 0; i--) {
            ret = Math.min(ret, 1 + calcSquares(n - i * i, history));
        }
        history[n] = ret;
        return history[n];
    }
    public int numSquares(int n) {
        int [] history = new int[n + 1];
        Arrays.fill(history, -1);
        history[0] = 0;
        return calcSquares(n, history);

    }

    public static void main(String[] args) {
        PerfectSquares perfectSquares = new PerfectSquares();
        int ret;
        ret = perfectSquares.numSquares(12);
        System.out.println(ret);
        ret = perfectSquares.numSquares(1);
        System.out.println(ret);
        ret = perfectSquares.numSquares(13);
        System.out.println(ret);
        ret = perfectSquares.numSquares(4);
        System.out.println(ret);
        ret = perfectSquares.numSquares(5);
        System.out.println(ret);

        ret = perfectSquares.numSquares(6);
        System.out.println(ret);

        ret = perfectSquares.numSquares(8);
        System.out.println(ret);
        ret = perfectSquares.numSquares(52);
        System.out.println(ret);
    }
}
