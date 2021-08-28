import java.util.Arrays;

public class CountingBits {
    public int[] countBits(int n) {
        int index = (int) (Math.pow(2, 3) - 1);
        int[] answer = new int[n + 1];
        System.out.println(index);
        System.out.println(2 & 3);
        for (int i = 0; i <= n; i++) {
            int k = i;
            while(k >= 1) {
                if(k % 2 == 1) answer[i]++;
                k /= 2;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        CountingBits countingBits = new CountingBits();
        int[] ret;
        ret = countingBits.countBits(5);
        Arrays.stream(ret).forEach(e -> System.out.print(e + " "));
    }
}
