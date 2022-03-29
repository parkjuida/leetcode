object LongestContinuousIncreasingSubsequence extends App {
  def findLengthOfLCIS(nums: Array[Int]): Int = {
    var prevNum = nums(0)
    var answer = 1
    var tempAnswer = 1
    for(i <- 1 until nums.length) {
      if(prevNum < nums(i)) {
        tempAnswer += 1
        answer = Math.max(tempAnswer, answer)
      } else {
        tempAnswer = 1
      }
      prevNum = nums(i)
    }
    answer
  }

  println(findLengthOfLCIS(Array(1)))
  println(findLengthOfLCIS(Array(1, 3, 5, 4, 7)))
  println(findLengthOfLCIS(Array(2, 2, 2, 2, 2)))
  println(findLengthOfLCIS(Array(1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7, 1, 3)))
}
