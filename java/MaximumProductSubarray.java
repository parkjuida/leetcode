public class MaximumProductSubarray {
    public int maxProduct(int[] nums) {
        int answer = Math.max(nums[0], nums[nums.length - 1]);
        int current_positive = nums[0];
        int current = nums[0];
        int current_back_positive = nums[nums.length - 1];
        int current_back = nums[nums.length - 1];

        if(nums[0] == 0) {
            current = 1;
        }
        if(nums[0] < 0) {
            current_positive = 1;
        }
        if(nums[nums.length - 1] == 0) {
            current_back = 1;
        }
        if(nums[nums.length - 1] < 0) {
            current_back_positive = 1;
        }

        for(int i = 1; i < nums.length; i++) {
            current = current * nums[i];
            current_positive = current_positive * nums[i];
            current_back = current_back * nums[nums.length - i - 1];
            current_back_positive = current_back_positive * nums[nums.length - i - 1];
            answer = Math.max(answer, Math.max(Math.max(current, current_positive), Math.max(current_back_positive, current_back)));
            if(current_positive < 0) {
                current_positive = 1;
            }
            if(current == 0) {
                current = 1;
            }
            if(current_back == 0) {
                current_back = 1;
            }
            if(current_back_positive < 0) {
                current_back_positive = 1;
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        MaximumProductSubarray mps = new MaximumProductSubarray();
        System.out.println(mps.maxProduct(new int[]{0, 2}));
        System.out.println(mps.maxProduct(new int[]{2, 2, 0, 2, 2, -2, -2, -2}));
        System.out.println(mps.maxProduct(new int[]{-2, 0, -1}));
        System.out.println(mps.maxProduct(new int[]{-2, 0, -1, 2, 3, -2, 4, 5}));
        System.out.println(mps.maxProduct(new int[]{2, -5, -2, -4, 3}));
        System.out.println(mps.maxProduct(new int[]{-1, -1, 0}));
        System.out.println(mps.maxProduct(new int[]{-1, -2, -3, 0}));
        System.out.println(mps.maxProduct(new int[]{-1, 0, -2, 2}));
    }
}
