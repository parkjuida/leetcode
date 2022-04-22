import scala.collection.mutable
import scala.collection.mutable.ListBuffer

class DesignHashMap {
  val MAX_SIZE = 1000
  val storage: Array[ListBuffer[(Int, Int)]] = Array.ofDim[mutable.ListBuffer[(Int, Int)]](MAX_SIZE)

  def put(key: Int, value: Int): Unit = {
    val hashValue = key % MAX_SIZE
    if(storage(hashValue) == null) {
      storage(hashValue) = new ListBuffer()
    }
    val list = storage(hashValue)
    if(list.find(l => l._1 == key).getOrElse((-1, -1))._1 != -1) {
      for (i <- list.indices) {
        if (list(i)._1 == key) {
          list(i) = (key, value)
        }
      }
    } else {
      list.addOne((key, value))
    }
  }

  def get(key: Int): Int = {
    val list = storage(key % MAX_SIZE)
    if(list == null) return -1
    val value = list.find { case (k, _) => key == k }
    value match {
      case Some(x) => x._2
      case _ => -1
    }
  }

  def remove(key: Int): Unit = {
    val list = storage(key % MAX_SIZE)
    if(list == null) return
    val data = list.zipWithIndex.find({case (data, index) => data._1 == key})
    data match {
      case Some(x) => list.remove(x._2)
      case _ =>
    }
  }

}

object DesignHashMap {
  def main(args: Array[String]): Unit = {
    var obj = new DesignHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    obj.get(1)
    obj.get(3)
  }
}
