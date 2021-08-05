import java.util.ArrayList;
import java.util.List;

public class FizzBuzz {
    public List<String> fizzBuzz(int n) {
        ArrayList<String> answer = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            if(i % 15 == 0) answer.add("FizzBuzz");
            else if(i % 5 == 0) answer.add("Buzz");
            else if(i % 3 == 0) answer.add("Fizz");
            else answer.add(String.valueOf(i));
        }

        return answer;
    }

    public static void main(String[] args) {
        FizzBuzz fb = new FizzBuzz();
        List<String> result = fb.fizzBuzz(3);
        result.stream().forEach(System.out::println);
        result = fb.fizzBuzz(5);
        result.stream().forEach(System.out::println);
        result = fb.fizzBuzz(15);
        result.stream().forEach(System.out::println);

    }
}
