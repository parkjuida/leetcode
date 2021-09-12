public class FibonacciNumber {

    public int fib(int n) {
        if(n == 0) return 0;
        if(n == 1) return 1;

        int prevPrev = 0;
        int prev = 1;
        int temp;

        for(int i = 2; i <= n; i++) {
            temp = prev;
            prev = prev + prevPrev;
            prevPrev = temp;
        }

        return prev;
    }

    public static void main(String[] args) {
        FibonacciNumber fibonacciNumber = new FibonacciNumber();
        System.out.println(fibonacciNumber.fib(2));
        System.out.println(fibonacciNumber.fib(3));
        System.out.println(fibonacciNumber.fib(4));
        System.out.println(fibonacciNumber.fib(5));
        System.out.println(fibonacciNumber.fib(6));
    }
}
