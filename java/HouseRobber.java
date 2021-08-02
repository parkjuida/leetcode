import java.util.Arrays;

public class HouseRobber {
    public int rob(int index, int[] nums, int[] history) {
        if(index >= nums.length) {
            return 0;
        }
        if(history[index] > -1) {
            return history[index];
        }
        history[index] = nums[index] + Math.max(rob(index + 3, nums, history), rob(index + 2, nums, history));
        return history[index];
    }

    public int rob(int[] nums) {
        int[] history = new int[nums.length];
        Arrays.fill(history, -1);
        return Math.max(rob(0, nums, history), rob(1, nums, history));

    }

    public static void main(String[] args) {
        HouseRobber hr = new HouseRobber();
        System.out.println(hr.rob(new int[]{1, 2, 3, 1}));
        System.out.println(hr.rob(new int[]{2, 7, 9, 3, 1}));
        System.out.println(hr.rob(new int[]{1}));
        System.out.println(hr.rob(new int[]{1, 3}));
        System.out.println(hr.rob(new int[]{ 3, 10, 5}));
    }
}
