import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class LetterCombinationsOfAPhoneNumber {
    public List<String> letterCombinations(String digits) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        ArrayList<String> candidates = new ArrayList<>();
        ArrayList<String> answers = new ArrayList<>();

        int number;
        for(char digit: digits.toCharArray()) {
            number = (digit - '0' - 2) * 3;
            if(digit == '7') {
                candidates.add(alphabet.substring(number, number + 4));
            } else if(digit == '8') {
                candidates.add(alphabet.substring(number + 1, number + 4));
            } else if(digit == '9') {
                candidates.add(alphabet.substring(number + 1, number + 5));
            } else {
                candidates.add(alphabet.substring(number, number + 3));
            }
        }

        for(String candidate: candidates) {
            if(answers.isEmpty()) {
                for(char c : candidate.toCharArray()) {
                    answers.add(String.valueOf(c));
                }
            } else {
                for(int i = answers.size(); i > 0; i--) {
                    String a = answers.remove(0);
                    for(char c : candidate.toCharArray()) {
                        answers.add(a.concat(String.valueOf(c)));
                    }
                }
            }
        }

        return answers;
    }
}
