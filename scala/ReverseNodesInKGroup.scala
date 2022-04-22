import scala.collection.mutable

object ReverseNodesInKGroup extends App {
  def reverseKGroup(head: ListNode, k: Int): ListNode = {
    var precede, posterior = head
    val stack = mutable.Stack[Int]()
    while(precede != null) {
      var counter = 0
      while(precede != null && counter < k) {
        stack.push(precede.x)
        precede = precede.next
        counter += 1
      }
      if(counter < k) return head
      while(stack.nonEmpty) {
        posterior.x = stack.pop()
        posterior = posterior.next
      }
    }
    head
  }


}
