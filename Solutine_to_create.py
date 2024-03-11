def reverse(self):
   prev_node = None
   current_node = self.head
   while current_node is not None:
       next_node = current_node.next
       current_node.next = prev_node
       prev_node = current_node
       current_node = next_node
   self.head, self.tail = self.tail, self.head