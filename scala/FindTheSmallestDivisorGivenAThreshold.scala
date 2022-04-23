import scala.util.control.Breaks.{break, breakable}

object FindTheSmallestDivisorGivenAThreshold extends App {
  def smallestDivisor(nums: Array[Int], threshold: Int): Int = {
    var left = 1
    var right = nums.max
    var currentBest = 10000000
    breakable {
      while (left <= right) {
        val mid = (left + right) / 2
        val divisionSum = nums.map(num => Math.ceil(num.toDouble / mid.toDouble)).sum
        val difference = threshold - divisionSum.toInt
        if (difference >= 0) {
          if(mid < currentBest) {
            currentBest = mid
          }
        }
        if (left == right) break
        if (difference >= 0) {
          right = mid - 1
        } else {
          left = mid + 1
        }
      }
    }
    currentBest
  }
  println(smallestDivisor(Array(1000000), 2))
//  println(smallestDivisor(Array(2,3,5,7,11), 11))
//  println(smallestDivisor(Array(1, 2, 5, 9), 6))
//  println(smallestDivisor(Array(44, 22, 33, 11, 1), 5))
//  println(smallestDivisor(Array(21212,10101,12121), 1000000))
}
