import scala.util.control.Breaks.{break, breakable}

object Solution extends App {
  def twoSum(nums: Array[Int], target: Int): Array[Int] = {
    for(i <- nums.indices) {
      for(j <- i + 1 until nums.length) {
        if(nums(i) + nums(j) == target) {
          return Array(i, j)
        }
      }
    }

    Array.emptyIntArray
  }

  println(twoSum(Array(2, 7, 11, 15), 9).mkString("[", ",", "]"))
  println(twoSum(Array(3, 2, 4), 6).mkString(","))
}