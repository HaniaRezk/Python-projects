class stack: #define class stack
    def __init__(self,n):
        self.v=[0]*n
        self.length=n
        self.top=-1

    def IsEmpty(self):
        if self.top==-1:
            return True
        return False

    def pop(self):
        if self.IsEmpty():
            return "error underflow"
        else:
            self.top-=1
            return self.v[self.top+1]

    def push(self,x):
        if self.top==self.length-1:
            return "error overflow"
        else:
            self.top+=1
            self.v[self.top]=x
            return self.v[self.top]

    def __repr__(self):
        return str(self.v)


class queue: #define class queue
    def __init__(self,n):
        self.v=[0]*n
        self.length=n
        self.tail=0
        self.head=0

    def enqueue(self,x):
        if self.tail==self.length:
            return "overflow"
        else:
            self.v[self.tail]=x
            if self.tail==self.length:
                self.tail=1
            else:
                self.tail+=1


    def Dequeue(self):
        if self.head==self.tail:
            return "error underflow"
        else:
            x=self.v[self.head]
            if self.head==self.length:
                self.head=1
            else:
                self.head=self.head+1
            return x

    def __repr__(self):
        return str(self.v)

def reverse(s):
    y=queue(len(s))
    for i in range(len(s)):
        y.enqueue(s.pop())
    return y

