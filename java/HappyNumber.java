import java.util.HashSet;

public class HappyNumber {
    public boolean isHappy(int n) {
        int unit = 10;
        int transformed = 0;
        HashSet<Integer> history = new HashSet<Integer>();

        while(true) {
            while (n != 0) {
                transformed += (n % unit) * (n % unit);
                n = n / unit;
            }

            if(history.contains(transformed)) {
                return false;
            }
            if(transformed == 1) {
                return true;
            }

            history.add(transformed);
            n = transformed;
            transformed = 0;
        }

    }

    public static void main(String[] args) {
        HappyNumber happyNumber = new HappyNumber();
        System.out.println(happyNumber.isHappy(19));
        System.out.println(happyNumber.isHappy(2));
    }
}
