from Queue import Queue
class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.right = None
      self.left = None
      self.subTreeHeight = 1

  def __init__(self):
    self.__root = None

  def insert_element(self, value):
    self.__root = self.__recursive_insert(value, self.__root)

  def __recursive_insert(self, val, node):
    if node is None:
      tempValue = None
    else:
      tempValue = node.value
    if node is None:
      new_node = Binary_Search_Tree.__BST_Node(val)
      node = new_node
    elif node.value == val:
      raise ValueError
    elif node.value > val:
      node.left = self.__recursive_insert(val, node.left)
    elif node.value < val:
      node.right = self.__recursive_insert(val, node.right)

    if (node.left is None) and (node.right is None):
      node.subTreeHeight = 1
    elif node.left is None:
      node.subTreeHeight = node.right.subTreeHeight + 1
    elif node.right is None:
      node.subTreeHeight = node.left.subTreeHeight + 1
    elif node.left.subTreeHeight >= node.right.subTreeHeight:
      node.subTreeHeight = node.left.subTreeHeight + 1
    else:
      node.subTreeHeight = node.right.subTreeHeight + 1

    return node

  def remove_element(self, value):
    self.__root = self.__recursive_remove(value, self.__root)


  def __recursive_remove(self, val, node):
    if node == None:
      raise ValueError

    elif node.value == val:
      if node.left is None:
        if node.right is None:
          return None
        else:
          return node.right

      else:
        if node.right is None:
          return node.left
        else:
          tempNode = node.right
          parentNode = node
          while tempNode.left is not None:
            parentNode = tempNode
            tempNode = tempNode.left
          if tempNode.right is not None:
            parentNode.left = tempNode.right
          else:
            parentNode.left = None
          node.value = tempNode.value
          return node

    else:
      if node.value > val:
        node.left = self.__recursive_remove(val, node.left)
        if (node.left is None) and (node.right is None):
          node.subTreeHeight = 1
        elif (node.left is None) and (node.right is not None):
          node.subTreeHeight = node.right.subTreeHeight + 1
        elif (node.left is not None) and (node.right is None):
          node.subTreeHeight = node.left.subTreeHeight + 1
        else:
          node.subTreeHeight = max(node.left.subTreeHeight, node.right.subTreeHeight) + 1
        return node

      else:
        node.right = self.__recursive_remove(val, node.right)
        if (node.left is None) and (node.right is None):
          node.subTreeHeight = 1
        elif (node.left is None) and (node.right is not None):
          node.subTreeHeight = node.right.subTreeHeight + 1
        elif (node.left is not None) and (node.right is None):
          node.subTreeHeight = node.left.subTreeHeight + 1
        else:
          node.subTreeHeight = max(node.left.subTreeHeight, node.right.subTreeHeight) + 1
        return node

  def in_order(self):
    if self.__root is None:
        in_order_string = "[ ]"
    else:
        temp_string = self.recursive_in_order(self.__root)
        temp_string = temp_string[2: ]
        in_order_string = str("[ " + temp_string + " ]")
    return in_order_string

  def recursive_in_order(self, node):
    my_string = ""
    if node.left is not None:
        my_string += self.recursive_in_order(node.left)

    my_string = my_string + ", " + str(node.value)

    if node.right is not None:
        my_string += self.recursive_in_order(node.right)

    return my_string

  def pre_order(self):
    if self.__root is None:
      return("[ ]")
    else:
      return( "[ " + str(self.__recursive_preorder(self.__root)[2:]) + " ]")

  def __recursive_preorder(self, node):
    if node is None:
      return ""
    else:
      return ", " + str(node.value) + str(self.__recursive_preorder(node.left)) + str(self.__recursive_preorder(node.right))

  def post_order(self):
    if self.__root is None:
      return("[ ]")
    else:
      return( "[ " + str(self.__recursive_postorder(self.__root)[2:]) + " ]")

  def __recursive_postorder(self, node):
    my_string = ""
    if node.left is not None:
      my_string += self.__recursive_postorder(node.left)

    if node.right is not None:
      my_string = my_string + self.__recursive_postorder(node.right)

    my_string = my_string + ", " + str(node.value)

    return my_string

  def breadth_first(self):
    if self.__root is None:
      return("[ ]")
    toQueue = Queue()
    output = "[ "
    toQueue.enqueue(self.__root)
    looping = True
    while looping == True:
      try:
        currNode = toQueue.dequeue()
        output = output + str(currNode.value) + ", "

        if currNode.left is not None:
          toQueue.enqueue(currNode.left)
        if currNode.right is not None:
          toQueue.enqueue(currNode.right)

      except IndexError:
        looping = False

    output = output[:-2]
    output = output + " ]"
    return output


  def get_height(self):
    if self.__root is None:
      return 0
    else:
      return self.__root.subTreeHeight

  def __str__(self):
    return self.in_order()

#if __name__ == '__main__':
