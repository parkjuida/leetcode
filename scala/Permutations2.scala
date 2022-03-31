import scala.collection.mutable
import scala.collection.mutable.ListBuffer

object Permutations2 extends App {
  def doPermuteUnique(numberCounter: mutable.SortedMap[Int, Int], currentState: ListBuffer[Int],
                      answer: ListBuffer[List[Int]]): Unit = {

    var nc = mutable.SortedMap.from(numberCounter)
    for(k <- numberCounter.keySet) {
      if(nc(k) > 0) {
        val cs: ListBuffer[Int] = currentState
        nc.update(k, nc(k) - 1)
        cs.addOne(k)
        doPermuteUnique(nc, cs, answer)
        cs.remove(cs.length - 1)
        nc.update(k, nc(k) + 1)
      } else {
        nc -= k
        if(nc.isEmpty) {
          answer.addOne(currentState.toList)
          return
        }
      }
    }
  }

  def permuteUnique(nums: Array[Int]): List[List[Int]] = {
    val toDo = mutable.SortedMap.from(nums.groupBy(num => num).map{
      case (k, v) => (k, v.length) })
    val answer = ListBuffer[List[Int]]()
    doPermuteUnique(toDo, ListBuffer(), answer)

    return answer.toList
  }

  println(permuteUnique(Array(1, 1, 2)))
  println(permuteUnique(Array(1, 2, 3)))
}
