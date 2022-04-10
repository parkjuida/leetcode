import scala.collection.mutable

object BaseballGame extends App {
  def calPoints(ops: Array[String]): Int = {
    val answer = mutable.Stack[Int]()
    ops.foreach((i: String) => {
      if(i == "+") {
        val last = answer.pop
        val newOne = answer.top + last
        answer.push(last)
        answer.push(newOne)
      } else if(i == "D") {
        answer.push(answer.top * 2)
      } else if(i == "C") {
        answer.pop()
      } else {
        answer.push(i.toInt)
      }
    })
    answer.sum
  }

  println(calPoints(Array("5", "2", "C", "D", "+")))
  println(calPoints(Array("5", "-2", "4", "C", "D", "9", "+", "+")))
  println(calPoints(Array("1")))
}
