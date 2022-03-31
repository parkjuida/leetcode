object CheckIfTheSentenceIsPangram extends App {
  def checkIfPangram(sentence: String): Boolean = {
    val set = sentence.toSet
    set.size == 'z' - 'a' + 1
  }

  println(checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
  println(checkIfPangram("leetcode"))
}
