import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class BasicCalculator2 {
    public void calc(Stack<Integer> numberStack, int currentNumber, char operand) {
        switch(operand) {
            case '+':
                numberStack.push(currentNumber);
                break;
            case '-':
                numberStack.push(-currentNumber);
                break;
            case '*':
                numberStack.push(numberStack.pop() * currentNumber);
                break;
            case '/':
                numberStack.push(numberStack.pop() / currentNumber);
                break;
        }
    }

    public int calculate(String s) {
        Stack<Integer> numberStack = new Stack<>();
        int currentNumber = 0;
        char operand = '+';
        for(char c: s.toCharArray()) {
            if(c == ' ') {
                continue;
            }
            if(Character.isDigit(c)) {
                currentNumber = currentNumber * 10 + c - '0';
            } else {
                calc(numberStack, currentNumber, operand);
                currentNumber = 0;
                operand = c;
            }
        }
        calc(numberStack, currentNumber, operand);

        int result = 0;
        while(!numberStack.empty()) {
            result += numberStack.pop();
        }

        return result;
    }

    public static void main(String[] args) {
        BasicCalculator2 bc2 = new BasicCalculator2();
        System.out.println(bc2.calculate("3 -2*2 + 4 / 2"));
    }
}
