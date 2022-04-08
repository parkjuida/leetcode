import scala.collection.mutable

class KthLargest(_k: Int, _nums: Array[Int]) {
  val queue = mutable.PriorityQueue[Int]().reverse
  _nums.foreach(i => queue.enqueue(i))

  def add(`val`: Int): Int = {
    queue.enqueue(`val`)
    while(queue.size > _k) {
      queue.dequeue()
    }

    queue.head
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    val kthLargest = new KthLargest(3, Array())
    println(kthLargest.add(3))
    println(kthLargest.add(5))
    println(kthLargest.add(10))
    println(kthLargest.add(9))
    println(kthLargest.add(4))
  }
}