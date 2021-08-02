import java.util.Arrays;

public class CountPrimes {
    public int countPrimes(int n) {
        boolean[] primes = new boolean[n];
        Arrays.fill(primes, true);

        for(int i = 2; i * i< n; i++) {
            if(!primes[i]) continue;
            for(int j = i * i; j < n; j = j + i) {
                primes[j] = false;
            }
        }
        int count = 0;
        for(int i = 2; i < n; i++) {
            if(primes[i]) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        CountPrimes countPrimes = new CountPrimes();
        System.out.println(countPrimes.countPrimes(10));
        System.out.println(countPrimes.countPrimes(0));
        System.out.println(countPrimes.countPrimes(2));
        System.out.println(countPrimes.countPrimes(14));
        System.out.println(countPrimes.countPrimes(499979));
    }
}
