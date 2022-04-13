object SpiralMatrix2 extends App {
  def generateMatrix(n: Int): Array[Array[Int]] = {
    var iterator = 1
    val answer = Array.ofDim[Int](n, n)
    var r, c = 0

    var step = n - 1
    while(iterator < n * n) {
      for(i <- 0 until step) {
        answer(r)(c) = iterator
        iterator += 1
        c += 1
      }
      for(i <- 0 until step) {
        answer(r)(c) = iterator
        iterator += 1
        r += 1
      }
      for(i <- 0 until step) {
        answer(r)(c) = iterator
        iterator += 1
        c -= 1
      }
      for(_ <- 0 until step) {
        answer(r)(c) = iterator
        iterator += 1
        r -= 1
      }
      r += 1
      c += 1
      step -= 2
    }
    if(n % 2 == 1) answer(r)(c) = iterator
    answer
  }

  var a = generateMatrix(6)
  a.foreach(e => println(e.mkString("[", ",", "]")))
  a = generateMatrix(4)
  a.foreach(e => println(e.mkString("[", ",", "]")))
  a = generateMatrix(1)
  a.foreach(e => println(e.mkString("[", ",", "]")))
  a = generateMatrix(5)
  a.foreach(e => println(e.mkString("[", ",", "]")))
}
