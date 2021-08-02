import java.util.Arrays;

public class HouseRobber {
    public int rob(int[] nums) {
        int valueOfAdjacent = nums[nums.length - 1];
        int valueOfNextAdjacent = 0;
        int value = 0;
        for(int i = nums.length - 2; i >= 0; i--) {
            value = Math.max(nums[i] + valueOfNextAdjacent, valueOfAdjacent);

            valueOfNextAdjacent = valueOfAdjacent;
            valueOfAdjacent = value;
        }

        return Math.max(value, valueOfAdjacent);
    }

    public static void main(String[] args) {
        HouseRobber hr = new HouseRobber();
        System.out.println(hr.rob(new int[]{1, 2, 3, 1}));
        System.out.println(hr.rob(new int[]{2, 7, 9, 3, 1}));
        System.out.println(hr.rob(new int[]{1}));
        System.out.println(hr.rob(new int[]{1, 3}));
        System.out.println(hr.rob(new int[]{ 3, 1, 5}));
    }
}
