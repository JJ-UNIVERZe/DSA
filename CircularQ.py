class CircularQueue:
   def __init__(self,maxsize):
      self.rear = -1
      self.front = -1
      self.maxsize = maxsize
      self.q = [None]*maxsize
   def IsFull(self):
      if (self.front == 0 and self.rear == self.maxsize-1) or (self.rear ==self.front-1) :
         return True
      else:
         return False
   def IsEmpty(self):
      if (self.rear== -1 and self.front==-1):
         return True
      else:
         return False
   def Enqueue(self,val):
      if self.IsFull():
         print("Circular Queue is Full")
      else:
         if self.rear == self.maxsize-1 :
            self.rear = 0
         else:
            self.rear += 1
            if self.front == -1:
               self.front +=1                                                                                                                                                                                                                                                                                  
         self.q[self.rear]=val
   def Dequeue(self):
      if self.IsEmpty():
         print("Circular Queue is Empty")
      else:
         idx = self.front
         if self.front == self.rear :
            self.rear = -1
            self.front = -1
         elif self.front == self.maxsize:
            self.front = 0
         else:
            self.front +=1
         self.q[idx] = None
   def display(self):
       print(self.q)
   def peek(self):
      if self.IsEmpty():
         print("Circular Queue is Empty")
      else:
         print("Peek Element is",self.q[self.front])
       
CQ = CircularQueue(5)
while True:
   print("---------------- Circular Queue Operations ---------------- ") 
   print("1.IsFull\n2.IsEmpty\n3.Enqueue\n4.Dequeue\n5.Peek\n6.Display")
   opt = int(input("Enter the option:\n"))
   match opt:
            case 1:
                print("Is stack Full-->",CQ.IsFull())
            case 2:
                print("Is stack Empty-->",CQ.IsEmpty())
            case 3:
                CQ.Enqueue(int(input("Enter the value:")))
            case 4:
                CQ.Dequeue()
            case 5:
                CQ.peek()
            case 6:
                CQ.display()
            case _:
                print("Invalid option.")