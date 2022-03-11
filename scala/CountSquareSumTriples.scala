object CountSquareSumTriples extends App {
  def cExist(a: Int, b: Int, n: Int): Boolean = {
    val c = Math.sqrt(a * a + b * b)
    if((c > n) || (c - c.toInt > 0)) false else true
  }

  def countTriples(n: Int): Int = {
    var answer = 0
    for(a <- 1 to n) {
      for(b <- a to n) {
        if(cExist(a, b, n)) {
          answer += 1
        }
      }
    }
    answer * 2
  }

  println(countTriples(5))
  println(countTriples(10))
  println(countTriples(13))
}
