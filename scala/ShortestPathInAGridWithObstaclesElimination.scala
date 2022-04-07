import scala.collection.mutable
import scala.util.control.Breaks.{break, breakable}

object ShortestPathInAGridWithObstaclesElimination extends App {
  def shortestPath(grid: Array[Array[Int]], k1: Int): Int = {
    val historyFromStart: Array[Array[mutable.Map[Int, Int]]] = Array
      .ofDim[mutable.Map[Int, Int]](grid.length, grid(0).length)
    val historyFromEnd: Array[Array[mutable.Map[Int, Int]]] = Array
      .ofDim[mutable.Map[Int, Int]](grid.length, grid(0).length)
    val m = grid.length
    val n = grid(0).length
    val k = Math.min(m + n, k1)
    val queue = mutable.Queue[(Int, Int, Int, Int)]()
    queue.enqueue((0, 0, k, 0))
    val MAX = 40 * 40 + 1

    def init(history: Array[Array[mutable.Map[Int, Int]]]) = {
      for(r <- 0 until m) {
        for(c <- 0 until n) {
          history(r)(c) = mutable.Map[Int, Int]()
        }
      }
    }
    init(historyFromStart)
    init(historyFromEnd)
    def search(history: Array[Array[mutable.Map[Int, Int]]]) = {
      val (r, c, _k, currentState) = queue.dequeue()
      if (history(r)(c).contains(_k)) {
        if (history(r)(c)(_k) > currentState) {
          history(r)(c).update(_k, currentState)
        } else break
      } else {
        history(r)(c).update(_k, currentState)
      }

      if (r - 1 >= 0) {
        if (grid(r - 1)(c) == 0) {
          if (history(r - 1)(c).getOrElse(_k, MAX) > currentState) queue.append((r - 1, c, _k, currentState + 1))
        } else {
          if (_k > 0 && history(r - 1)(c).getOrElse(_k - 1, MAX) > currentState) queue.append((r - 1, c, _k - 1, currentState + 1))
        }
      }

      if (c - 1 >= 0) {
        if (grid(r)(c - 1) == 0) {
          if (history(r)(c - 1).getOrElse(_k, MAX) > currentState) queue.append((r, c - 1, _k, currentState + 1))
        } else {
          if (_k > 0 && history(r)(c - 1).getOrElse(_k - 1, MAX) > currentState) queue.append((r, c - 1, _k - 1, currentState + 1))
        }
      }

      if (c < n - 1) {
        if (grid(r)(c + 1) == 0) {
          if (history(r)(c + 1).getOrElse(_k, MAX) > currentState) queue.append((r, c + 1, _k, currentState + 1))
        } else {
          if (_k > 0 && history(r)(c + 1).getOrElse(_k - 1, MAX) > currentState) queue.append((r, c + 1, _k - 1, currentState + 1))
        }
      }

      if (r < m - 1) {
        if (grid(r + 1)(c) == 0) {
          if (history(r + 1)(c).getOrElse(_k, MAX) > currentState) queue.append((r + 1, c, _k, currentState + 1))
        } else {
          if (_k > 0 && history(r + 1)(c).getOrElse(_k - 1, MAX) > currentState) queue.append((r + 1, c, _k - 1, currentState + 1))
        }
      }
    }

    while(queue.nonEmpty) {
      breakable {
        search(historyFromStart)
      }
    }
    
    queue.enqueue((m - 1, n - 1, k, 0))
    while(queue.nonEmpty) {
      breakable {
        search(historyFromEnd)
      }
    }

    var answer = 40 * 40 + 1
    for(r <- grid.indices) {
      for(c <- grid(0).indices) {
        var minFromStart: (Int, Int) = (MAX, MAX)
        for(tuples <- historyFromStart(r)(c)) {
          if(minFromStart._2 > tuples._2) minFromStart = tuples
        }
        for(tuples <- historyFromEnd(r)(c)) {
          if(minFromStart._1 + tuples._1 >= k) {
            answer = Math.min(answer, minFromStart._2 + tuples._2)
          }
        }
      }
    }

    if(answer >= 40 * 40 + 1) -1 else answer
//    println(m, n)
//    for(r <- 0 until m) {
//      for(c <- 0 until n) {
//        println(s"$r $c map: ${historyFromStart(r)(c)}")
//      }
//    }
  }

  println(shortestPath(
    Array(
      Array(0, 1, 0, 1),
      Array(0, 1, 0, 0),
      Array(0, 0, 1, 0),
      Array(1, 0, 0, 1),
      Array(0, 1, 0, 0),
    ), 18
  ))
  println(shortestPath(
    Array(
      Array(0, 1, 1),
      Array(1, 1, 1),
      Array(1, 0, 0),
    ), 1
  ))
  println(shortestPath(
    Array(
      Array(0),
    ), 1
  ))


}
