
object Shift2DGrid extends App {
  def shiftGrid(grid: Array[Array[Int]], k: Int): List[List[Int]] = {
    val flattened = grid.flatten
    val newOne = flattened.indices.map(i => {
      var index = (i - k) % flattened.length
      if(index < 0) index += flattened.length
      flattened(index)
    })

    for(i <- grid.indices) {
      for(j <- grid(0).indices) {
        grid(i)(j) = newOne(i * grid(0).length + j)
      }
    }

    val answer = grid.map(_.toList).toList

    answer
  }

  println(shiftGrid(Array(Array(1, 2, 3), Array(4, 5, 6), Array(7, 8, 9)), 1))
  println(shiftGrid(Array(Array(1), Array(2), Array(3), Array(4)), 23))
}
