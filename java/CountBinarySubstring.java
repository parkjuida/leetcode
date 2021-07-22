public class CountBinarySubstring {
    public int countBinarySubstrings(String s) {
        int countZero = 0, countOne = 0, answer = 0;
        char prevChar = ' ';
        for(char c: s.toCharArray()) {
            if(c == '0') {
                if(prevChar == '1') {
                    countZero = 0;
                }
                countZero++;
                if(countOne > 0) {
                    countOne--;
                    answer++;
                }
            }

            if(c == '1') {
                if(prevChar == '0') {
                    countOne = 0;
                }
                countOne++;
                if(countZero > 0) {
                    countZero--;
                    answer++;
                }
            }
            prevChar = c;
        }

        return answer;
    }

    public static void main(String[] args) {
        CountBinarySubstring cb = new CountBinarySubstring();
        int result = cb.countBinarySubstrings("110100");
        System.out.println(result);
    }
}
