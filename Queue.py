# Linear Queue with Limited Size
class Queue:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.q = []
    def IsFull(self):
        if len(self.q) == self.maxsize:
            return True
        else:
            return False
    def IsEmpty(self):
        if len(self.q) == 0:
            return True
        else:
            return False
    def Enqueue(self,val):
        if self.IsFull():
            print("Queue is Full")
        else:
            self.q.append(val)
    def Dequeue(self):
        if self.IsEmpty():
            print("Queue has 0 elements")
        else:
            self.q.pop(0)
    def Display(self):
        if self.IsEmpty():
            print("Queue has no elements")
        else:
            print(self.q)

q1 = Queue(5)
while True:
    print("-------------- Queue Operations --------------")
    print("1.IsFull\n2.IsEmpty\n3.Enqueue\n4.Dequeue\n5.Peek\n6.Display")
    opt = int(input("Enter the option:\n"))
    match opt:
        case 1:
            print("Is stack Full-->",q1.IsFull())
        case 2:
            print("Is stack Empty-->",q1.IsEmpty())
        case 3:
            q1.Enqueue(int(input("Enter the value:")))
        case 4:
            q1.Dequeue()
        case 5:
            q1.peek()
        case 6:
            q1.Display()
        case _:
            print("Invalid option.")
