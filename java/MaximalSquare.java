import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

public class MaximalSquare {
    public int find(char[][] matrix, int row, int col) {
        if(matrix[row][col] == '0') {
            return 0;
        }
        int answer = 0;
        for(int size = 0; size < 300; size++) {
            if(col + size == matrix[0].length || row + size == matrix.length) {
                return answer;
            }
            for(int c = col; c <= col + size; c++) {
                if(matrix[row + size][c] == '0') {
                    return answer;
                }
            }
            for(int r = row; r < row + size; r++) {
                if(matrix[r][col + size] == '0') {
                    return answer;
                }
            }
            answer = (size + 1) * (size + 1);
        }
        return answer;
    }

    public int maximalSquare(char[][] matrix) {
        int answer = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                answer = Math.max(answer, find(matrix, i, j));
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        MaximalSquare maximalSquare = new MaximalSquare();
        int ret = maximalSquare.maximalSquare(new char[][]{{'0', '1'}, {'1', '0'}});
        System.out.println(ret);
        ret = maximalSquare.maximalSquare(new char[][]{{'0'}});
        System.out.println(ret);
        ret = maximalSquare.maximalSquare(new char[][]{
                {'1', '0', '1', '0', '0'},
                {'1', '0', '1', '1', '1'},
                {'1', '1', '1', '1', '1'},
                {'1', '0', '0', '1' ,'0'}
        });
        System.out.println(ret);

        ret = maximalSquare.maximalSquare(new char[][]
                {
                        {'0','0','0','1','0','1','1','1'},
                        {'0','1','1','0','0','1','0','1'},
                        {'1','0','1','1','1','1','0','1'},
                        {'0','0','0','1','0','0','0','0'},
                        {'0','0','1','0','0','0','1','0'},
                        {'1','1','1','0','0','1','1','1'},
                        {'1','0','0','1','1','0','0','1'},
                        {'0','1','0','0','1','1','0','0'},
                        {'1','0','0','1','0','0','0','0'}
                });
        System.out.println(ret);
    }
}

