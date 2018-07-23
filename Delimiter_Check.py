import sys # for sys.argv, the command-line arguments
from Stack import Stack
def delimiter_check(filename):
  # returns True if the delimiters (), [], and {} are balanced and False otherwise.
  file_object = open(filename,"r")
  file_string = str(file_object.read())
  file_stack = Stack()
  for i in file_string:
    if i== "(" or i=="[" or i=="{":
        file_stack.push(i)
    elif i == ")":
        stack_top = file_stack.pop()
        if stack_top != "(":
            return False
    elif i == "}":
        stack_top = file_stack.pop()
        if stack_top != "{":
            return False
    elif i == "]":
        stack_top = file_stack.pop()
        if stack_top != "[":
            return False
  if len(file_stack)==0:
    return True
  else:
    return False


if __name__ == '__main__':

  if len(sys.argv) < 2:

    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')
