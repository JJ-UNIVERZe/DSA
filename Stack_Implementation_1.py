# Stack Implementaion without limited size
class Stack:
    def __init__(self):
        self.s1 = []
    def display(self):
        if len(self.s1) != 0:
            for i in range(len(self.s1)-1,-1,-1):
                print(self.s1[i])
        else:
            print("Stack has 0 elements")
    def push(self,val):
        self.s1.append(val) # self.s1 += [val] / self.s1.append(val)
    def pop(self):
        self.s1.pop()
    def peek(self):
        if len(self.s1) !=0:
           print("Top element is :",self.s1[-1])
        else:
            print("Stack has 0 elements")
st = Stack()
while True:
    print("-------------- Stack Operations --------------")
    print("1.Push\n2.Pop\n3.Peek\n4.Display")
    opt = int(input("Enter the option:\n"))
    match opt:
        case 1:
            st.push(int(input("Enter the value:")))
        case 2:
            st.pop()
        case 3:
            st.peek()
        case 4:
            st.display()
        case _:
            print("Invalid option.")