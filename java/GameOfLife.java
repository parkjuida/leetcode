import java.util.Arrays;

public class GameOfLife {
    public void update(int[][] countOfLives, int row, int col) {
        for(int i = row - 1; i <= row + 1; i++) {
            for(int j = col - 1; j <= col + 1;j++) {
                if(i < 0 || j < 0 || i >= countOfLives.length || j >= countOfLives[0].length
                || (i == row && j == col)) {
                    continue;
                }
                countOfLives[i][j]++;
            }
        }
    }

    public void gameOfLife(int[][] board) {
        // 1 -> 0: 2 이하의 1 또는 4이상의 1
        // 1 -> 1: 2~3 의 1
        // 0 -> 1: 3개의 1
        int[][] countOfLives = new int[board.length][board[0].length];

        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                if(board[i][j] == 0) {
                    continue;
                }
                update(countOfLives, i, j);
            }
        }

        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                if(board[i][j] == 0) {
                    if(countOfLives[i][j] == 3) {
                        board[i][j] = 1;
                    }
                }
                if(board[i][j] == 1) {
                    int count = countOfLives[i][j];
                    if(count < 2 || count > 3) {
                        board[i][j] = 0;
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        GameOfLife gol = new GameOfLife();
        int [][] state = new int[][]{
                {0, 1, 0},
                {0, 0, 1},
                {1, 1, 1},
                {0, 0, 0},
        };
        gol.gameOfLife(state);
        for(int i = 0; i < state.length; i++) {
            System.out.println(Arrays.toString(state[i]));
        }

        state = new int[][]{
                {1, 1},
                {1, 0}
        };
        gol.gameOfLife(state);
        for(int i = 0; i < state.length; i++) {
            System.out.println(Arrays.toString(state[i]));
        }
    }
}
