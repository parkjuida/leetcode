public class MinimumPathSum {
    public int minPathSum(int[][] grid) {
        for(int row = 0; row < grid.length; row++) {
            for(int col = 0; col < grid[0].length; col++) {
                int temp = grid[row][col];
                if(row - 1 >= 0) {
                    grid[row][col] = temp + grid[row - 1][col];
                }
                if(col - 1 >= 0) {
                    if(grid[row][col] == temp) {
                        grid[row][col] = temp + grid[row][col - 1];
                    } else {
                        grid[row][col] = Math.min(grid[row][col], grid[row][col - 1] + temp);
                    }
                }
            }
        }

        return grid[grid.length - 1][grid[0].length - 1];
    }

    public static void main(String[] args) {
        MinimumPathSum mps = new MinimumPathSum();
        int [][] grid;
        grid = new int[][]{{1, 3, 1}, {1, 5, 1}, {4, 2, 1}};
        System.out.println(mps.minPathSum(grid));
        grid = new int[][]{{1,2,3},{4,5,6}};
        System.out.println(mps.minPathSum(grid));
    }
}
