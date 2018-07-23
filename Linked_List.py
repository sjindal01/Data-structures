class Linked_List:

  class __Node: #internal, private class; basic unit of the doubly linked list
    def __init__(self, val): #Node constructor
      self.prev = None #pointer to previous node, initially None (must be manually set after Node constructor is called)
      self.value = val #value that the node contains
      self.nex = None #pointer to next node, initially None (must be manually set after Node constructor is called)

  def __init__(self): #Linked_List constructor
    self.__size = 0 #internally managed size/length variable, 0 for a new linked list
    self.__header = Linked_List.__Node(None) #beginning sentinel, contains value 'None'
    self.__trailer = Linked_List.__Node(None) #end sentinel, contains value 'None'
    self.__header.nex = self.__trailer #header forward points to trailer
    self.__trailer.prev = self.__header #trailer backward points to header

  def __len__(self):
    return self.__size


  def append_element(self, val): #add element to the end of the list
    new_node = Linked_List.__Node(val) #declare a new node
    new_node.prev = self.__trailer.prev #new_node's previous element should be the 'old' last element of the list
    new_node.nex = self.__trailer #the new node's next element should be trailer

    self.__trailer.prev.nex = new_node #make the 'old' last element of the list forward point to the new last element, i.e. new_node

    self.__trailer.prev = new_node #trailer's previous is new_node

    self.__size += 1 #increment the size by 1

  def insert_element_at(self, val, index):

    if index < 0 or index >= self.__size: #you cannot add after the last element (aka append) with this method; you must use the append method for that
        raise IndexError #we don't like negative or superfluous indexes; raise exception

    current = 0
    current_node = self.__header

    while current < index: #'current walk' to the element one before index; to the 'index-1'th element
        current_node = current_node.nex
        current += 1

	#current_node is element 'index-1', current_node.nex is element 'index'

    new_node = Linked_List.__Node(val)  #initialize new_node with value 'val'
    new_node.nex = current_node.nex #since new_node will displace whatever is at 'index' forward, it should forward point to that which it displaces
    new_node.prev = current_node #new_node should backpoint to the 'index-1'th element, aka 'current_node'


    current_node.nex.prev = new_node #the element at position 'index' should back-point to new_node
    current_node.nex = new_node #the element at position 'index-1' should forward point to new_node, which is now at position 'index'

    self.__size += 1 #increment size by 1

  def remove_element_at(self, index):

    if index < 0 or index >= self.__size: #no negative or out of bounds indices; if list is empty, index 0 is invalid because index == size
       raise IndexError

    current = 0
    current_node = self.__header

    while current <= index: #'current walk' to the 'index'th element
        current_node = current_node.nex
        current += 1

    #after the loop, current_node represents the node we are removing

    val = current_node.value #save the value of the to be removed node
    current_node.prev.nex = current_node.nex #make the node before current_node forward point to the node after current_node
    current_node.nex.prev = current_node.prev #make the node after current_node back-point to the node before current_node

    #current_node is effectively removed since the linked_list retains no reference to it after the termination of this method
    #garbage collector will formalize its removal
    current_node.prev = None #in case the user is removing multiple elements, it's best not to retain any 'ghost' pointers, because these could prevent the garbage
    current_node.nex = None  #collector from removing certain elements (unpredictability of when the garbage collector actually frees memory, and in what order memory freeing is done)

    self.__size -= 1 #decrement the size

    return val #return the value of the removed element, as per the project specifications

  def get_element_at(self, index):

    if index < 0 or index >= self.__size:
       raise IndexError

    current = 0
    current_node = self.__header

    while current <= index: #current walk to 'index'th element
        current_node = current_node.nex
        current += 1

    return current_node.value


  def rotate_left(self):
    first_node = self.__header.nex.value #save the first node in memory

    self.remove_element_at(0) #remove the 0th element, which will inherently shift every element in the list down one
    self.append_element(first_node) #re-add the first node at the end, effectively simulating a circular rotate left

  def __str__(self): #represent the linked_list object as a string, looks kind of like an array representation but with spaces

    if self.__size == 0:
        return "[ ]"
    else:
        ret_str ="[ "

        current_node = self.__header.nex #initialize current_node to the first node

        for i in range(self.__size-1): #append the values of all nodes in the linked list; if the list has length 1 this loop will not execute
            ret_str += str(current_node.value) + ", "
            current_node = current_node.nex


        ret_str += str(current_node.value) + " ]" #append the last node's value

        return ret_str

  def __iter__(self):

    self.__iter_node = self.__header #declare a node for iteration

    return self

  def __next__(self): #returns the next node

    if self.__iter_node.nex is self.__trailer: #the only node that forward points to trailer is the last node; we don't want to return trailer so raise an exception
        raise StopIteration

    self.__iter_node = self.__iter_node.nex

    return self.__iter_node.value

if __name__ == '__main__':

	####### Test cases to verify that the linked_list class functions properly #######
	####### These test cases were implented such that if no exceptions were raised, then the test cases all passed #######

    test_list_size = 10

	#Test case 1: get_element_at()
	#Does get_element_at() correctly fetch elements at given indices, raising exceptions for invalid indices?

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    for i in range(test_list_size):
        if test_list.get_element_at(i) != i:
            print("Test case 1 failed; fetching element " + str(i) + " did not return " + str(i) + " as expected.")
            quit()
    try:
        test_list.get_element_at(-1)
        print("Test case 1 failed; fetching at a negative index did not raise an exception.")
        quit()
    except IndexError:
         pass

    try:
        test_list.get_element_at(99999)
        print("Test case 1 failed; fetching at a too large index did not raise an exception.")
        quit()
    except IndexError:
         pass

	#Test case 2: append()
	#Does appending to the list add an element at the new tail position and increment the size by one?
    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

        if len(test_list) != i + 1:
            print("Test case 2 failed; appending an element to the list did not correctly increment the size of the list.")
            quit()

        if test_list.get_element_at(i) != i:
            print("Test case 2 failed; appending an element to the list did not place the element at the tail position.")
            quit()

	#Test case 3: insert_element_at()
	#Does inserting an item at a valid index increase the size by one and correctly modify the list's structure?
	#Does inserting an item at an invalid index raise an exception and leave the list completely unchanged?

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    test_list.insert_element_at(999,0)

    if len(test_list) != test_list_size + 1:
         print("Test case 3 failed; inserting an element at position 0 did not correctly increment the size.")
         quit()

    if test_list.get_element_at(0) != 999:
         print("Test case 3 failed; inserting an element at position 0 did not correctly place the element.")
         quit()

    test_list.insert_element_at(888,7)

    if len(test_list) != test_list_size + 2:
         print("Test case 3 failed; inserting an element at position 7 did not correctly increment the size.")
         quit()

    if test_list.get_element_at(7) != 888:
         print("Test case 3 failed; inserting an element at position 7 did not correctly place the element.")
         quit()

    test_list = Linked_List()

    try:
        test_list.insert_element_at(555, 0)
        print("Test case 3 failed; inserting into index 0 of an empty list did not raise an exception.")
        quit()
    except IndexError:
        pass

    for i in range(test_list_size):
        test_list.append_element(i)

    try:
        test_list.insert_element_at(888, -1)
        print("Test case 3 failed; inserting at a negative index did not raise an exception.")
        quit()
    except IndexError:
         for i in range(test_list_size):
            if test_list.get_element_at(i) != i:
                print("Test case 3 failed; inserting an element at a negative index has modified the list somehow.")
                quit()

    try:
        test_list.insert_element_at(999, test_list_size)
        print("Test case 3 failed; inserting at the tail position did not raise an exception.")
        quit()
    except IndexError:
         for i in range(test_list_size):
            if test_list.get_element_at(i) != i:
                print("Test case 3 failed; inserting an element at the tail position has modified the list somehow.")
                quit()

    try:
        test_list.insert_element_at(777, 9999999)
        print("Test case 3 failed; inserting at a too large index did not raise an exception.")
        quit()
    except IndexError:
         for i in range(test_list_size):
            if test_list.get_element_at(i) != i:
                print("Test case 3 failed; inserting an element at a too large index has modified the list somehow.")
                quit()

	#Test case 4: remove_element_at()
	#Does removing an item at a valid index decrease the size by one and correctly modify the list's structure?
	#Does removing an item at an invalid index raise an exception and leave the list completely unchanged?
    #Does removing the only item in a list of length 1 work, and is the size 0?
    #Does trying to remove an element from an empty list raise an exception?
    #After removing the last element in a list, do trailer and header to point to each other as in the beginning? (i.e. is the list reusable?)

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    test_list.remove_element_at(0)

    if len(test_list) != test_list_size - 1:
        print("Test case 4 failed: removing element 0 did not decrement the size of the list.")
        quit()

    for i in range(test_list_size - 1):
        if test_list.get_element_at(i) == 0 or test_list.get_element_at(i) != i + 1:
            print("Test case 4 failed: removing an element at index 0 did not properly remove the element and shift down all other elements.")
            quit()

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    test_list.remove_element_at(3)

    if len(test_list) != test_list_size - 1:
        print("Test case 4 failed; removing element 3 did not decrement the size of the list.")
        quit()

    for i in range(test_list_size - 1):
        if test_list.get_element_at(i) == 3:
            print("Test case 4 failed; removing an element at index 3 did not properly remove the element and shift down all other elements.")
            quit()

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    try:
        test_list.remove_element_at(-1)
        print("Test case 4 failed; trying to remove at a negative index did not raise an exception.")
        quit()
    except IndexError:
         for i in range(test_list_size):
            if test_list.get_element_at(i) != i:
                print("Test case 4 failed; trying to remove at a negative index has modified the list somehow.")
                quit()

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    try:
        test_list.remove_element_at(999)
        print("Test case 4 failed; trying to remove at a too large index did not raise an exception.")
        quit()
    except IndexError:
         for i in range(test_list_size):
            if test_list.get_element_at(i) != i:
                print("Test case 4 failed; trying to remove at a too large index has modified the list somehow.")
                quit()

    test_list = Linked_List()

    test_list.append_element(999)

    test_list.remove_element_at(0)

    try:
        test_list.get_element_at(0)
        print("Test case 4 failed; fetching element 0 of an emptied list did not raise an exception")
        quit()
    except IndexError:
        pass


    if len(test_list) != 0:
        print("Test case 4 failed: after removing from a list of length 1, the length of the list is not 0.")
        quit()

    try:
        test_list.remove_element_at(0)
        print("Test case 4 failed; trying to remove an element from an empty list did not raise an exception.")
        quit()
    except IndexError:
        pass

    for i in range(test_list_size):
        test_list.append_element(i)

    for i in range(test_list_size):
        if test_list.get_element_at(i) != i:
            print("Test case 4 failed; appending into a list that was previously emptied does not place elements properly (do header and trailer point to each other after removal of the last element?")
            quit()


    test_list = Linked_List()

    if len(test_list) != 0:
        print("Test case 5 failed; length of a newly initialized list is not 0.")
        quit()

    test_list.append_element(999)

    if len(test_list) != 1:
        print("Test case 5 failed; length of a singleton list is not 1.")
        quit()

    for i in range(test_list_size):
        test_list.insert_element_at(50,0)

    if len(test_list) != test_list_size + 1:
        print("Test case 5 failed; length of a list after performing insert_element_at is incorrect.")
        quit()

    for i in range(test_list_size):
        test_list.remove_element_at(0)

    if len(test_list) != 1:
        print("Test case 5 failed; length of a list after performing remove_element_at is incorrect.")
        quit()


    test_list = Linked_List()

    if str(test_list) != "[ ]":
        print("Test case 6 failed; string representation of empty list is incorrect (" + str(test_list) + ")")
        quit()

    test_list.append_element(1)

    if str(test_list) != "[ 1 ]":
        print("Test case 6 failed; string representation of singleton list is incorrect (" + str(test_list) + ")")
        quit()

    test_list.append_element(2)
    test_list.append_element(3)

    if str(test_list) != "[ 1, 2, 3 ]":
        print("Test case 6 failed; string representation of several-element list is incorrect (" + str(test_list) + ")")
        quit()


    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    i = 0

    for val in test_list:
        if val != test_list.get_element_at(i):
            print("Test case 7 failed; iterating through a linked list did not provide the elements of the linked list in the proper order.")
            quit()
        i += 1


    test_list = Linked_List()

    try:
        test_list.rotate_left()
        print("Test case 8 failed; attempting to rotate an empty list left did not raise an exception.")
        quit()
    except:
        pass

    test_list.append_element(999)
    test_list.rotate_left()

    if test_list.get_element_at(0) != 999:
        print("Test case 8 failed; rotating a singleton list left improperly modified the list.")
        quit()

    test_list = Linked_List()

    for i in range(test_list_size):
        test_list.append_element(i)

    test_list.rotate_left()

    if test_list.get_element_at(0) == 0 or test_list.get_element_at(test_list_size - 1) != 0:
        print("Test case 8 failed; rotating a list left did not place the first element at the end of the list.")
        quit()

    for i in range(test_list_size - 1):
        if test_list.get_element_at(i) != i + 1:
            print("Test case 8 failed; rotating a list left shift over all elements to the left.")
            quit()

    print("All test cases passed!")
