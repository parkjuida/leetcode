class UniquePaths2 {
    fun uniquePathsWithObstacles(obstacleGrid: Array<IntArray>): Int {
        val height = obstacleGrid.size
        val width = obstacleGrid[0].size
        val answer = Array(height) {Array(width) {0} }

        if((height == 1 && width == 1) || obstacleGrid[0][0] == 1) {
            answer[0][0] = 0
        }
        for(i in obstacleGrid.indices) {
            for(j in obstacleGrid[0].indices) {
                if(obstacleGrid[i][j] != 1) {
                    if(i == 0 && j == 0 ) answer[0][0] = 1
                    else if (i == 0) answer[i][j] = answer[i][j - 1]
                    else if(j == 0) answer[i][j] = answer[i - 1][j]
                    else {
                        answer[i][j] = answer[i - 1][j] + answer[i][j - 1]
                    }
                }
            }
        }

        return answer[height - 1][width - 1]
    }

}


fun main(args: Array<String>) {
    val s = UniquePaths2()
    val arr1 = arrayOf(
        intArrayOf(1, 0)
    )
    println(s.uniquePathsWithObstacles(arr1))
    val arr2 = arrayOf(
        intArrayOf(1, 1, 1),
        intArrayOf(1, 1, 1),
        intArrayOf(1, 1, 1),
    )
    println(s.uniquePathsWithObstacles(arr2))
}