import scala.collection.mutable

object LastStoneWeight extends App {
  def lastStoneWeight(stones: Array[Int]): Int = {
    val pq = mutable.PriorityQueue.from(stones)

    while(pq.size > 1) {
      val mostHeavy = pq.dequeue()
      val secondHeavy = pq.dequeue()
      val diff = Math.abs(secondHeavy - mostHeavy)
      if(diff > 0) pq.enqueue(diff)
    }
    if(pq.isEmpty) 0 else pq.dequeue()
  }

  println(lastStoneWeight(Array(2, 7, 4, 1, 8, 1)))
  println(lastStoneWeight(Array(1)))
  println(lastStoneWeight(Array(1, 1000)))
  println(lastStoneWeight(Array(1, 2, 3)))

}
