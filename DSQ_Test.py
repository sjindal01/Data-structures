import unittest
from Deque_Generator import get_deque, LL_DEQUE_TYPE, ARR_DEQUE_TYPE
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):

    def setUp(self):
    # Run tests with each deque type to ensure that
    # they behave identically.
        self.__deque = get_deque(LL_DEQUE_TYPE)
        self.__stack = Stack()
        self.__queue = Queue()

    #empty test:
    def test_Empty_Deque(self):
        self.assertEqual('[ ]', str(self.__deque), 'Empty deque should print as "[ ]"')
        self.assertEqual('[ ]', str(self.__queue), 'Empty queue should print as "[ ]"')
        self.assertEqual('[ ]', str(self.__stack), 'Empty stack should print as "[ ]"')

    #empty peek test and empty string peek
    def test_f_b_indentical_deque(self):
        self.assertEqual(self.__deque.peek_back(), self.__deque.peek_front())
    def test_peek_empty_f(self):
        self.assertEqual(None, self.__deque.peek_front())
    def test_peek_empty_f_str(self):
        self.assertEqual("None", str(self.__deque.peek_front()))
    def test_peek_empty_b(self):
        self.assertEqual(None, self.__deque.peek_back())
    def test_peek_empty_b_str(self):
        self.assertEqual("None", str(self.__deque.peek_back()))
    def test_peek_empty_stack(self):
        self.assertEqual(None, self.__stack.peek())
    def test_peek_empty_stack_str(self):
        self.assertEqual("None", str(self.__stack.peek()) )
    #empty pop error check:
    def test_pop_f_deque_empty(self):
        with self.assertRaises(IndexError):
            self.__deque.pop_front()
    def test_pop_b_deque_empty(self):
        with self.assertRaises(IndexError):
            self.__deque.pop_back()
    def test_pop_stack_empty(self):
        with self.assertRaises(IndexError):
            self.__stack.pop()
    def test_dequeue_queue_empty(self):
        with self.assertRaises(IndexError):
            self.__queue.dequeue()
    #empty len() check:
    def test_len_function_empty_deque(self):
        self.assertEqual(0, len(self.__deque))
    def test_len_function_empty_stack(self):
        self.assertEqual(0, len(self.__stack))
    def test_len_function_empty_queue(self):
        self.assertEqual(0, len(self.__queue))

    #Adding one element test:
    def test_adding_one_element_b(self):
        self.__deque.push_back(1)
        self.assertEqual(1, len(self.__deque))
        self.assertEqual('[ 1 ]', str(self.__deque))
    def test_peek_f_b_one_element_deque(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.peek_front())
        self.assertEqual(1, self.__deque.peek_back())
    def test_peek_f_b_one_element_deque_str(self):
        self.__deque.push_back(1)
        self.assertEqual("1", str(self.__deque.peek_front()))
        self.assertEqual("1", str(self.__deque.peek_back()))
    def test_adding_one_element_f(self):
        self.__deque.push_front(1)
        self.assertEqual(1, len(self.__deque))
        self.assertEqual('[ 1 ]', str(self.__deque))
    def test_peek_f_b_one_element_deque(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.peek_front())
        self.assertEqual(1, self.__deque.peek_back())
    def test_peek_f_b_one_element_deque_str(self):
        self.__deque.push_front(1)
        self.assertEqual("1", str(self.__deque.peek_front()))
        self.assertEqual("1", str(self.__deque.peek_back()))
    def test_adding_one_element_stack(self):
        self.__stack.push(1)
        self.assertEqual(1, len(self.__stack))
        self.assertEqual('[ 1 ]', str(self.__stack))
    def test_peek_one_element_stack(self):
        self.__stack.push(1)
        self.assertEqual(1, self.__stack.peek())
    def test_peek_one_element_stack_str(self):
        self.__stack.push(1)
        self.assertEqual("1", str(self.__stack.peek()))
    def test_adding_one_element_queue(self):
        self.__queue.enqueue(1)
        self.assertEqual(1, len(self.__queue))
        self.assertEqual('[ 1 ]', str(self.__queue))
    def test_pop_one_element_deque_b_b(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.pop_back())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_one_element_deque_f_b(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.pop_back())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_one_element_deque_b_f(self):
        self.__deque.push_back(1)
        self.assertEqual(1, self.__deque.pop_front())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_one_element_deque_f_f(self):
        self.__deque.push_front(1)
        self.assertEqual(1, self.__deque.pop_front())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_two_element_deque_error_b(self):
        self.__deque.push_back(1)
        self.__deque.pop_back()
        with self.assertRaises(IndexError):
            self.__deque.pop_back()
    def test_pop_two_element_deque_error_f(self):
        self.__deque.push_back(1)
        self.__deque.pop_front()
        with self.assertRaises(IndexError):
            self.__deque.pop_front()

    #Adding two element test:
    def test_adding_two_element_b_deque(self):
        self.__deque.push_back(1)
        self.__deque.push_back(2)
        self.assertEqual(2, len(self.__deque))
        self.assertEqual('[ 1, 2 ]', str(self.__deque))
    def test_adding_two_element_f_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, len(self.__deque))
        self.assertEqual('[ 2, 1 ]', str(self.__deque))
    def test_adding_two_element_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.assertEqual(2, len(self.__stack))
        self.assertEqual('[ 2, 1 ]', str(self.__stack))
    def test_adding_two_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.assertEqual(2, len(self.__queue))
        self.assertEqual('[ 1, 2 ]', str(self.__queue))
    def test_peek_f_f_two_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_front(2)
        self.assertEqual(2, self.__deque.peek_front())
        self.assertEqual(1, self.__deque.peek_back())
    def test_peek_f_b_two_element_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.assertEqual(1, self.__deque.peek_front())
        self.assertEqual(2, self.__deque.peek_back())
    def test_pop_one_two_element_deque_f(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.assertEqual(1, self.__deque.pop_front())
        self.assertEqual("[ 2 ]", str(self.__deque))
    def test_pop_one_two_element_deque_b(self):
        self.__deque.push_back(1)
        self.__deque.push_front(2)
        self.assertEqual(2, self.__deque.pop_front())
        self.assertEqual("[ 1 ]", str(self.__deque))
    def test_pop_two_slement_deque_to_empty_f(self):
        self.__deque.push_back(1)
        self.__deque.push_front(2)
        self.assertEqual(2, self.__deque.pop_front())
        self.assertEqual(1, self.__deque.pop_front())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_two_slement_deque_to_empty_f(self):
        self.__deque.push_back(1)
        self.__deque.push_front(2)
        self.assertEqual(1, self.__deque.pop_back())
        self.assertEqual(2, self.__deque.pop_back())
        self.assertEqual("[ ]", str(self.__deque))
    def test_pop_f_b_reassign_deque(self):
        self.__deque.push_front(1)
        self.__deque.push_back(2)
        self.__deque.pop_front()
        self.assertEqual(self.__deque.peek_front(), self.__deque.peek_back())





    #Multiple element add and removal( comprehensive test case):
    def test_adding_peek_six_element_deque_random(self):
        self.__deque.push_back(6)
        self.__deque.push_front(1)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_back(5)
        self.assertEqual('[ 3, 2, 1, 6, 4, 5 ]', str(self.__deque))
        self.assertEqual(3, self.__deque.peek_front())
        self.assertEqual(5, self.__deque.peek_back())
    def test_remove_peek_two_element_back_deque(self):
        self.__deque.push_back(6)
        self.__deque.push_front(1)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_back(5)
        self.__deque.pop_back()
        self.__deque.pop_back()
        self.assertEqual(3, self.__deque.peek_front())
        self.assertEqual(6, self.__deque.peek_back())
        self.assertEqual('[ 3, 2, 1, 6 ]', str(self.__deque))
    def test_remove_peek_two_element_front_deque(self):
        self.__deque.push_back(6)
        self.__deque.push_front(1)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_back(5)
        self.__deque.pop_front()
        self.__deque.pop_front()
        self.assertEqual(1, self.__deque.peek_front())
        self.assertEqual(5, self.__deque.peek_back())
        self.assertEqual('[ 1, 6, 4, 5 ]', str(self.__deque))
    def test_remove_all_element_front_peek_deque(self):
        self.__deque.push_back(6)
        self.__deque.push_front(1)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_back(5)
        i=0
        while i!=6:
            self.__deque.pop_front()
            i+=1
        self.assertEqual(None, self.__deque.peek_front())
        self.assertEqual(None, self.__deque.peek_back())
        self.assertEqual('[ ]', str(self.__deque))
    def test_remove_all_element_back_peek_deque(self):
        self.__deque.push_back(6)
        self.__deque.push_front(1)
        self.__deque.push_back(4)
        self.__deque.push_front(2)
        self.__deque.push_front(3)
        self.__deque.push_back(5)
        i=0
        while i!=6:
            self.__deque.pop_back()
            i+=1
        self.assertEqual(None, self.__deque.peek_front())
        self.assertEqual(None, self.__deque.peek_back())
        self.assertEqual('[ ]', str(self.__deque))

    def test_adding_four_element_peek_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.assertEqual(4, self.__stack.peek())
        self.assertEqual('[ 4, 3, 2, 1 ]', str(self.__stack))
    def test_removing_two_element_peek_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        self.__stack.pop()
        self.__stack.pop()
        self.assertEqual(2, self.__stack.peek())
        self.assertEqual('[ 2, 1 ]', str(self.__stack))
    def test_removing_all_element_stack(self):
        self.__stack.push(1)
        self.__stack.push(2)
        self.__stack.push(3)
        self.__stack.push(4)
        i=0
        while i!=4:
            self.__stack.pop()
            i+=1
        self.assertEqual(None, self.__stack.peek())
        self.assertEqual('[ ]', str(self.__stack))
    def test_adding_four_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.assertEqual('[ 1, 2, 3, 4 ]', str(self.__queue))
    def test_removing_two_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        self.__queue.dequeue()
        self.__queue.dequeue()
        self.assertEqual('[ 3, 4 ]', str(self.__queue))
    def test_removing_all_element_queue(self):
        self.__queue.enqueue(1)
        self.__queue.enqueue(2)
        self.__queue.enqueue(3)
        self.__queue.enqueue(4)
        i=0
        while i!=4:
            self.__queue.dequeue()
            i+=1
        self.assertEqual('[ ]', str(self.__queue))


if __name__ == '__main__':
  unittest.main()
