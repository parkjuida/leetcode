public class NthTribonacciNumber {
    public int tribonacci(int n) {
        if(n == 0) return 0;
        if(n < 3) return 1;

        int prevPrevPrev = 0, prevPrev = 1, prev = 1;
        int temp;
        for(int i = 3; i <= n; i++) {
            temp = prev;
            prev = prev + prevPrev + prevPrevPrev;
            prevPrevPrev = prevPrev;
            prevPrev = temp;
        }

        return prev;
    }

    public static void main(String[] args) {
        NthTribonacciNumber nthTribonacciNumber = new NthTribonacciNumber();
        System.out.println(nthTribonacciNumber.tribonacci(4));
        System.out.println(nthTribonacciNumber.tribonacci(25));
    }
}
