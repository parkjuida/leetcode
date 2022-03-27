object TheKWeakestRowsInAMatrix extends App {
  def kWeakestRows(mat: Array[Array[Int]], k: Int): Array[Int] = {
      mat.zipWithIndex.map { case (arr, index) => (arr.sum, index)}
        .sorted
        .map { case (_, index) => index }.take(k)
  }

  println(kWeakestRows(
    Array(
      Array(1, 1, 0, 0, 0),
      Array(1, 1, 1, 1, 0),
      Array(1, 0, 0, 0, 0),
      Array(1, 1, 0, 0, 0),
      Array(1, 1, 1, 1, 1)
    ), 3
  ).mkString("Array(", ", ", ")"))
  println(kWeakestRows(
    Array(
      Array(1, 0, 0, 0),
      Array(1, 1, 1, 1),
      Array(1, 0, 0, 0),
      Array(1, 0, 0, 0),
    ), 2
  ).mkString("Array(", ", ", ")"))

}
