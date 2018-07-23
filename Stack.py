from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self._dq = get_deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def push(self, val):
    self._dq.push_front(val)

  def pop(self):
    return self._dq.pop_front()
    
  def peek(self):
    return self._dq.peek_front()


#if __name__ == '__main__':
