
class Buffer1:
    def __init__(self, size):
        self.arr = [0]*size
        self.header = 0
        self.size = size
        self.begin = 0

    def Get(self):
        return self.arr
    
    def Front(self):
        return self.arr[self.begin]
    
    def Put(self, value):
        if self.header == self.size:
            self.header = 0
        self.arr[self.header] = value
        self.header += 1

    def Pop(self):
        if self.begin < self.header:
            self.begin += 1
        else:
            self.begin = 0

b = Buffer1(3)
b.Put(1)
b.Put(33)
print(b.Get())
b.Put(444)
print(b.Get())
b.Put(555)
print(b.Get())



class Buffer2:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def Put(self, value):
        self.Recursion1(value)
        self.Recursion2()
    
    def Pop(self):
        self.stack2.pop()
    

    def Front(self):
        return self.stack2[0]

    def Size(self):
        return len(self.stack2)


    
    def Recursion1(self, value):
        if len(self.stack2) == 0:
            self.stack1.append(value)
        else:
            self.stack1.append(self.stack2[-1])
            self.stack2.pop()
            self.Recursion1(value)
    
    def Recursion2(self):
        if len(self.stack1) == 0: 
            return
        else:
            self.stack2.append(self.stack1[-1])
            self.stack1.pop()
            self.Recursion2()

    def Get(self):
        return self.stack2

buf = Buffer2()
buf.Put(1)
buf.Put(2)
buf.Put(3)
buf.Put(4)
buf.Put(5)
print(buf.Front())
print(buf.Get())
buf.Pop()
buf.Pop()
print(buf.Front())
print(buf.Get())