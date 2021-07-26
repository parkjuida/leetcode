import java.util.Arrays;
import java.util.Stack;

public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();
        String[] operands = new String[]{"+", "*", "/", "-"};

        for(String token:tokens) {
            if(Arrays.asList(operands).contains(token)) {
                int b = stack.pop(), a = stack.pop(), result = 0;
                if(token.equals("+")) {
                    result = a + b;
                } else if(token.equals("*")) {
                    result = a * b;
                } else if (token.equals("-")) {
                    result = a - b;
                } else if(token.equals("/")) {
                    result = a / b;
                }
                stack.push(result);
            } else {
                stack.push(Integer.parseInt(token));
            }
        }

        return stack.pop();
    }

    public static void main(String[] args) {
        EvaluateReversePolishNotation ev = new EvaluateReversePolishNotation();
        System.out.println(ev.evalRPN(new String[]{"2", "1", "+", "3", "*"}));
        System.out.println(ev.evalRPN(new String[]{"4", "13", "5", "/", "+"}));
        System.out.println(ev.evalRPN(new String[]{"10","6","9","3","+","-11","*","/","*","17","+","5","+"}));
    }
}
