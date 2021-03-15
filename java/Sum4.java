import java.util.*;

public class Sum4 {
    public void solve() {
        System.out.println(this.fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0));
        System.out.println(this.fourSum(new int[]{}, 0));
    }

    public List<List<Integer>> fourSum(int[] nums, int target) {
        int[] arr = Arrays.stream(nums).sorted().toArray();
        HashSet<List<Integer>> answer = new HashSet<>();

        for(int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                int left = j + 1;
                int right = arr.length - 1;
                while (left < right) {
                    int s = arr[i] + arr[j] + arr[left] + arr[right];
                    if (s < target) {
                        left++;
                    } else if (s > target) {
                        right--;
                    } else {
                        answer.add(new ArrayList<>(Arrays.asList(arr[i], arr[j], arr[left], arr[right])));
                        left++;
                        right--;
                    }
                }
            }
        }

        return new ArrayList(answer);
    }
}
