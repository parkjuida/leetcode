import java.util.Arrays;

public class MissingNumber {
    public int missingNumber(int[] nums) {
        int n = nums.length;
        int s = Arrays.stream(nums).sum();

        return n * (n + 1) / 2 - s;
    }

    public static void main(String[] args) {
        MissingNumber missingNumber = new MissingNumber();
        int result;
        result = missingNumber.missingNumber(new int[]{3, 0, 1});
        System.out.println(result);
        result = missingNumber.missingNumber(new int[]{0, 1});
        System.out.println(result);
        result = missingNumber.missingNumber(new int[]{9, 6, 4, 2, 3, 5, 7, 0, 1});
        System.out.println(result);
        result = missingNumber.missingNumber(new int[]{0});
        System.out.println(result);
    }
}
