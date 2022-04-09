import scala.collection.immutable.ListMap

object TopKFrequentElements extends App {
  def topKFrequent(nums: Array[Int], k: Int): Array[Int] = {
    val frequency = nums.groupBy(i => i)
      .map{ case (key, values) => (key, values.length)}
    frequency.toSeq.sortBy(_._2).reverse.take(k).map(_._1).toArray
  }

  println(topKFrequent(Array(1, 1, 1, 2, 2, 3), 2).mkString("Array(", ", ", ")"))
  println(topKFrequent(Array(1), 1).mkString("Array(", ", ", ")"))
}
