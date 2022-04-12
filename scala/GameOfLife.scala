object GameOfLife extends App {
  def setValue(i: Int, j: Int, board: Array[Array[Int]], value: Int): Unit = {
    try {
      board(i)(j) += value
    } catch {
      case _: Exception =>
    }
  }

  def gameOfLife(board: Array[Array[Int]]): Unit = {
    val m = board.length
    val n = board(0).length

    val newBoard = Array.ofDim[Int](m, n)
    for(i <- 0 until m) {
      for(j <- 0 until n) {
        setValue(i + 1, j, newBoard, board(i)(j))
        setValue(i , j + 1, newBoard, board(i)(j))
        setValue(i - 1, j + 1, newBoard, board(i)(j))
        setValue(i + 1, j + 1, newBoard, board(i)(j))
        setValue(i + 1, j - 1, newBoard, board(i)(j))
        setValue(i - 1, j, newBoard, board(i)(j))
        setValue(i, j - 1, newBoard, board(i)(j))
        setValue(i - 1, j - 1, newBoard, board(i)(j))
      }
    }

    for(i <- 0 until m) {
      for(j <- 0 until n) {
        if(board(i)(j) == 1) {
          board(i)(j) = if(newBoard(i)(j) < 2) {
            0
          } else if(newBoard(i)(j) <= 3) {
            1
          } else 0
        } else {
          if(newBoard(i)(j)  == 3) {
            board(i)(j) = 1
          } else {
            board(i)(j) = 0
          }
        }
      }
    }

  }


  val a = Array(
      Array(0, 1, 0),
      Array(0, 0, 1),
      Array(1, 1, 1),
      Array(0, 0, 0),
    )

  println(a.map(_.mkString("[", ",", "]")).mkString("Array(", ", ", ")"))
  gameOfLife(a)
  println(a.map(_.mkString("[", ",", "]")).mkString("Array(", ", ", ")"))
}
