import scala.collection.mutable

object MaximumNumberOfGroupsGettingFreshDonuts extends App {
  def preprocess(batchSize: Int, count: mutable.Map[Int, Int]): Int = {
    var answer = 0
    answer += count(0)
    count -= 0

    for(key <- 1 to batchSize / 2) {
      val min = Math.min(count(key), count(batchSize - key))
      if(batchSize - key != key) {
        count(key) -= min
        count(batchSize - key) -= min
        answer += min
      } else {
        count(key) -= min / 2 * 2
        answer += min/2
      }

      if(count(key) == 0) {
        count -= key
      }
      if(count(batchSize - key) == 0) {
        count -= (batchSize - key)
      }
    }
    answer
  }

  def find(
            batchSize: Int,
            prevDonut: Int,
            count: mutable.Map[Int, Int],
            memo: mutable.Map[Map[Int, Int], Int]): Int = {
    val status: Map[Int, Int] = count.toMap
    if (memo.contains(status)) {
      memo(status)
    } else if (count.isEmpty) {
      0
    } else {
      var max = 0
      for(i <- count.keys) {
        count(i) -= 1
        if(count(i) < 1) count -= i
        max = Math.max(max, find(batchSize, (prevDonut + i) % batchSize, count, memo))

        count(i) += 1
      }
      memo(status) = if(prevDonut == 0) max + 1 else max
      memo(status)
    }
  }

  def maxHappyGroups(batchSize: Int, groups: Array[Int]): Int = {
    val count = mutable.Map[Int, Int]().withDefaultValue(0)
    val memo = mutable.Map[Map[Int, Int], Int]().withDefaultValue(0)
    groups.foreach(group => count(group % batchSize) += 1)
    preprocess(batchSize, count) + find(batchSize, 0, count, memo)
  }

  println(maxHappyGroups(2, Array(1, 1, 2, 2, 1)))
  println(maxHappyGroups(4, Array(1, 3, 2, 5, 2, 2, 1, 6)))
  println(maxHappyGroups(1, Array(1)))
  println(maxHappyGroups(1, Array(2, 3, 4)))
  println(maxHappyGroups(2, Array(1)))
  println(
    maxHappyGroups(
      2,
        Array(1,0,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1)
    )
  )
  println(
    maxHappyGroups(
      7,
      Array(287773481,815094798,356732984,644469322,543193620,903158817,274116865,395252956,363839119,365378492,122313059,312690039,252532812)
    )
  )
  println(
    maxHappyGroups(
      3,
      Array(369821235,311690424,74641571,179819879,171396603,274036220)
    )
  )
  println(
    maxHappyGroups(9,
    Array(3,1,3,3,5,6,1,1,9,10,3,3,3,1,1,3,3,3,19,20,1,3,3,3,3,1,1,3,3,30))
  )
}

