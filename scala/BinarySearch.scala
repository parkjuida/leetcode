import scala.util.control.Breaks
import scala.util.control.Breaks.{break, breakable}

object BinarySearch extends App {
  def search(nums: Array[Int], target: Int): Int = {
    var (l, r) = (0, nums.length - 1)

    while(l <= r) {
      val c = (l + r) / 2
      if(nums(c) == target) return c
      else if(nums(c) < target) l = c + 1
      else r = c - 1
    }
    -1
  }

  println(search(Array(-1, 0, 3, 5, 9, 12), 9))
  println(search(Array(-1, 0, 3, 5, 9, 12), 2))
  println(search(Array(5), 3))
  println(search(Array(1, 2), 3))

}
