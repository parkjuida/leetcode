import java.util.Arrays;
import java.util.Comparator;

public class RussianDollEnvelopes {
    public boolean compareEnvelops(int[] a, int[] b) {
        if(a[0] < b[0] && a[1] < b[1]) {
            return true;
        }
        return false;
    }

    public int maxEnvelopes(int[][] envelops) {
        Arrays.sort(envelops, Comparator.comparingInt(e ->((int []) e)[0]).thenComparingInt(e -> ((int []) e)[1]));
        int[] history = new int[envelops.length];
        boolean canMerge;
        int counter = 0;

        for(int i = 0; i < envelops.length; i++) {
            canMerge = false;
            for(int j = i - 1; j >= 0; j--) {
                if(compareEnvelops(envelops[j], envelops[i])) {
                    canMerge = true;
                    history[i] = Math.max(history[i], history[j] + 1);
                }
            }
            if(!canMerge) {
                history[i] = 1;
            }
            counter = Math.max(counter, history[i]);
        }

        return counter;
    }

    public static void main(String[] args) {
        RussianDollEnvelopes rde = new RussianDollEnvelopes();
        int result;
        result = rde.maxEnvelopes(new int[][]{{1, 100}, {2, 2}, {3, 3}});
        System.out.println(result);

        result = rde.maxEnvelopes(new int[][]{{1, 1}, {1, 1}, {1, 1}});
        System.out.println(result);

        result = rde.maxEnvelopes(new int[][]{{5, 4}, {6, 4}, {6, 7}, {2, 3}});
        System.out.println(result);

        result = rde.maxEnvelopes(new int[][]{{46, 89}, {50, 53}, {52, 68}, {72, 45}, {77, 81}});
        System.out.println(result);
    }
}
