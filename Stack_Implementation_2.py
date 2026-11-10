# Stack Implementation with limited size

class Stack:
    def __init__(self,maxsize):
        self.s1 = []
        self.maxsize = maxsize
    def IsFull(self):
        if self.s1.__len__() == self.maxsize:
            return True
        else:
            return False
    def IsEmpty(self):
        if self.s1.__len__() == 0:
            return True
        else:
            return False
    def push(self,val):
        if self.IsFull():
            print("Stack is Full")
        else:
            self.s1.append(val)
    def pop(self,val):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self.s1.pop()
    def peek(self):
        if self.IsEmpty():
            print("Stack is Empty")
        else:
            print("Top Element is:-->",self.s1[-1])
    def display(self):
        if self.s1.__len__() == 0:
            print("Stack is Empty")
        else:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
st = Stack(5)
while True:
    print("-------------- Stack Operations --------------")
    print("1.IsFull\n2.IsEmpty\n3.Push\n4.Pop\n5.Peek\n6.Display")
    opt = int(input("Enter the option:\n"))
    match opt:
        case 1:
            print("Is stack Full-->",st.IsFull())
        case 2:
            print("Is stack Empty-->",st.IsEmpty())
        case 3:
            st.push(int(input("Enter the value:")))
        case 4:
            st.pop()
        case 5:
            st.peek()
        case 6:
            st.display()
        case _:
            print("Invalid option.")