import scala.collection.mutable

object LongestValidParentheses extends App {
  def longestValidParentheses(s: String): Int = {
    val validParenthesesStack = mutable.Stack[(Int, Int, Int)]()
    val tempStack = mutable.Stack[(Int, Int)]()

    for(i <- s.indices) {
      if(s(i) == '(') {
        tempStack.push((s(i), i))
      } else {
        if(tempStack.isEmpty) {
          tempStack.push((s(i), i))
        } else {
          if(tempStack.top._1 == '(') {
            val (_, index) = tempStack.pop()
            validParenthesesStack.push((2, index, i))
          } else {
            tempStack.push((s(i), i))
          }
        }
      }
    }

    var answer = 0
    if(validParenthesesStack.isEmpty) {
      answer
    } else {
      var tempState = validParenthesesStack.pop()
      var tempAnswer = 0
      answer = tempState._1
      while(validParenthesesStack.nonEmpty) {
        val currentTop = validParenthesesStack.pop()
        if(tempState._2 - 1 == currentTop._3) {
          tempAnswer = tempState._1 + currentTop._1
          answer = Math.max(answer, tempAnswer)
          tempState = (tempAnswer , currentTop._2, tempState._3)
        } else if (tempState._2 < currentTop._2 && tempState._3 > currentTop._3) {
          tempAnswer = tempState._1 + currentTop._1
          answer = Math.max(answer, tempAnswer)
          tempState = (tempAnswer, tempState._2, tempState._3)
        } else {
          tempAnswer = 0
          tempState = currentTop
        }
      }
      answer
    }

  }

  println(longestValidParentheses("()(())"))
  println(longestValidParentheses("()()()"))
  println(longestValidParentheses("())()()"))
  println(longestValidParentheses(")))))"))
  println(longestValidParentheses(""))
  println(longestValidParentheses("())(()))"))
  println(longestValidParentheses("((()))))()()(())"))
}
