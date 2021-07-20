import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

public class ReorderDataInLogFiles {
    public String[] reorderLogFiles(String[] logs) {
        Arrays.sort(logs, (string1, string2) -> {
            String[] strings1 = string1.split(" ", 2);
            String[] strings2 = string2.split(" ", 2);

            boolean isString1Digit = Character.isDigit(strings1[1].charAt(0));
            boolean isString2Digit = Character.isDigit(strings2[1].charAt(0));

            if(isString1Digit && isString2Digit) {
                return 0;
            } else if(!isString1Digit && isString2Digit) {
                return -1;
            } else if(isString1Digit && !isString2Digit) {
                return 1;
            } else {
                int result = strings1[1].compareTo(strings2[1]);
                if(result == 0) {
                    result = strings1[0].compareTo(strings2[0]);
                }
                return result;
            }

        });
        return logs;
    }

    public static void main(String[] args) {
        ReorderDataInLogFiles reorderDataInLogFiles = new ReorderDataInLogFiles();
        String[] input = new String[100];
        input[0] = "g1 act car";
        input[1] = "a8 act zoo";
        input[2] = "a2 act car";
        input[3] = "let2 own kit dig";
        input[4] = "let2 art can";
        String[] output = reorderDataInLogFiles.reorderLogFiles(input);
        for(String o:output) {
            System.out.print(o + " ");
        }
    }

}
