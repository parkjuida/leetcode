import scala.collection.mutable.ListBuffer

object SortArrayByParity extends App {
  def sortArrayByParity(nums: Array[Int]): Array[Int] = {
    val answer = ListBuffer[Int]()
    answer.addAll(nums.filter(_ % 2 == 0))
    answer.addAll(nums.filter(_ % 2 == 1))
    answer.toArray
  }

  println(sortArrayByParity(Array(3, 1, 2, 4)))
}
