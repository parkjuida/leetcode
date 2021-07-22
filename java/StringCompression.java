public class StringCompression {

    public int compress(char[] chars) {
        char tempChar = chars[0];
        int count = 1;
        int answer = 0;
        int index = 0;
        char [] answerCount;

        for(int i = 1; i < chars.length; i++) {
            if(chars[i] == tempChar) {
                count++;
            } else {
                chars[index++] = tempChar;
                answer++;

                if(count != 1) {
                    answerCount = Integer.toString(count).toCharArray();

                    for(char c: answerCount) {
                        chars[index++] = c;
                    }
                    answer += answerCount.length;
                }

                tempChar = chars[i];
                count = 1;
            }
        }
        chars[index++] = tempChar;
        answer++;

        if(count != 1) {
            answerCount = Integer.toString(count).toCharArray();

            for(char c: answerCount) {
                chars[index++] = c;
            }
            answer += answerCount.length;
        }

        return answer;
    }

    public static void main(String[] args) {
        StringCompression sc = new StringCompression();
        char[] input = new char[7];
        System.out.println(sc.compress(new char[]{'a', 'a', 'b', 'b', 'c', 'c', 'c'}));
        System.out.println(sc.compress(new char[]{'a'}));
        System.out.println(sc.compress(new char[]{'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'}));
        System.out.println(sc.compress(new char[]{'a', 'a', 'a', 'b', 'b', 'a', 'a'}));
    }
}
