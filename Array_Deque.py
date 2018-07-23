from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__size = 0
    self.__contents = [None] * self.__capacity
    self.__front=0
    self.__back=0


  def __str__(self):
    if self.__size == 0:
        string='[ ]'
    else:
        string = '[ '
        for i in range(self.__size-1):
            x = (self.__front + i) % len(self.__contents)
            string += str(self.__contents[x])
            string += ", "

        string += str(self.__contents[self.__back])
        string += ' ]'


    return string

  def __len__(self):
    return self.__size

  def __grow(self):
    a=[None]
    self.__capacity = self.__capacity*2
    a=a*self.__capacity
    for i in range(len(self.__contents)):
        x=(self.__front+i)% len(self.__contents)
        a[i]=self.__contents[x]
    self.__contents = a
    self.__front=0
    self.__back=self.__size-1


  def push_front(self, val):
    if self.__size+1 > self.__capacity:
        self.__grow()

    self.__front =(self.__front -1 + self.__capacity) % self.__capacity
    self.__contents[self.__front]=val
    self.__size +=1


  def pop_front(self):
    if self.__size==0:
        raise IndexError
    a=self.__contents[self.__front]
    self.__contents[self.__front]=None
    self.__front=(self.__front + 1 +self.__capacity)%self.__capacity
    self.__size -=1
    return a

  def peek_front(self):
    return self.__contents[self.__front]

  def push_back(self, val):
    if self.__size+1 > self.__capacity:
        self.__grow()
    if self.__size == 0:
        self.__contents[self.__back]=val
        self.__size+=1

    else:
        self.__back = self.__back + 1
        self.__contents[self.__back]=val
        self.__size+=1

  def pop_back(self):
    if self.__size==0:
        raise IndexError
    a=self.__contents[self.__back]
    self.__contents[self.__back]=None
    self.__back-=1
    self.__size-=1
    return a

  def peek_back(self):
    return self.__contents[self.__back]


#if __name__ == '__main__':
