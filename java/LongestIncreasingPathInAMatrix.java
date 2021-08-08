import java.util.Arrays;

public class LongestIncreasingPathInAMatrix {
    public int calculate(int[][] matrix, int[][] history, int row, int col, int m, int n) {
        if(history[row][col] > 1) {
            return history[row][col];
        }
        int ret = 1;
        if(row + 1 < m && matrix[row][col] < matrix[row + 1][col]) {
            ret = Math.max(ret, 1 + calculate(matrix, history, row + 1, col, m, n));
        }
        if(row - 1 >= 0 && matrix[row][col] < matrix[row - 1][col]) {
            ret = Math.max(ret, 1 + calculate(matrix, history, row - 1, col, m, n));
        }
        if(col + 1 < n && matrix[row][col] < matrix[row][col + 1]) {
            ret = Math.max(ret, 1 + calculate(matrix, history, row, col + 1, m, n));
        }
        if(col - 1 >= 0 && matrix[row][col] < matrix[row][col - 1]) {
            ret = Math.max(ret, 1 + calculate(matrix, history, row, col -1, m, n));
        }
        history[row][col] = ret;
        return history[row][col];
    }

    public int longestIncreasingPath(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int [][] history = new int[m][n];
        for(int[] h:history) {
            Arrays.fill(h, 0);
        }
        int answer = 1;
        for(int row = 0; row < matrix.length; row++) {
            for(int col = 0; col < matrix[0].length; col++) {
                answer = Math.max(answer, calculate(matrix, history, row, col, m, n));
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        LongestIncreasingPathInAMatrix longestIncreasingPathInAMatrix = new LongestIncreasingPathInAMatrix();
        int result;
        result = longestIncreasingPathInAMatrix.longestIncreasingPath(
                new int[][]{
                        {9, 9, 4},
                        {6, 6, 8},
                        {2, 1, 1}
                }
        );
        System.out.println(result);
        result = longestIncreasingPathInAMatrix.longestIncreasingPath(
                new int[][]{
                        {3, 4, 5},
                        {3, 2, 6},
                        {2, 2, 1}
                }
        );
        System.out.println(result);
        int[][] a = new int[200][200];
        for (int i = 0; i < 200; i++) {
            for(int j = 0; j < 200; j++) {
                a[i][j] = i + j;
            }
        }
        result = longestIncreasingPathInAMatrix.longestIncreasingPath(
              a
        );
        System.out.println(result);
    }
}
