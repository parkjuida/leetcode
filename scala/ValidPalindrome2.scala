import scala.collection.mutable

object ValidPalindrome2 extends App {
  def validPalindrome(s: String): Boolean = {
    val (l, r) = (0, s.length - 1)
    val q = mutable.Stack[(Int, Int)]()
    q.addOne((l, r))
    var chance = true
    while(q.nonEmpty) {
      val (left, right) = q.pop()
      if(left >= right) return true
      if(s(left) == s(right)) {
        q.addOne((left + 1, right - 1))
      } else if(chance) {
        chance = false
        q.addOne((left, right - 1))
        q.addOne((left + 1, right))
      }
    }
    false
  }

  println(validPalindrome("aba"))
  println(validPalindrome("abca"))
  println(validPalindrome("abc"))
  println(validPalindrome("dabcad"))
  println(validPalindrome("afkfga"))
}
