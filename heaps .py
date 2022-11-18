def parent(i):
    if i==0:
        return None
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def setmaxheap(A):
    if len(A)==0:
        return 0
    i=1
    while i<len(A) and A[parent(i)]>=A[i]:
        i+=1
    return i

class heap():
    def __init__(self,A):
        self.v=A
        self.length= len(A)
        self.heapsize= setmaxheap(A)

    def printArray(self):
        print(self.v)

    def getHeapsize(self):
        return self.heapsize

    def maxheapify(self,i): #heapify sorting algorithm 
        A=self.v
        l=left(i)
        r=right(i)
        largest=i
        if l<self.length and A[l]>A[i]:
            largest=l
        if r<self.length and A[r]>A[largest]:
            largest=r
        if largest != i:
            c=A[i]
            A[i]=A[largest]
            A[largest]=c
            self.maxheapify(largest)
        return A

    def buildmaxheap(self):
        A = self.v
        self.heapsize=self.length
        for i in range ((self.length-1)//2,0,-1):
            self.maxheapify(i)

    def heapsort(self):
        A=self.v
        self.buildmaxheap()
        for i in range (self.length-1,1,-1):
            a=A[0]
            A[0]=A[i]
            A[i]=a
            self.heapsize-=1
            self.maxheapify(0)
        print(A)


A=[12,5,9,3,0,8]
h=heap(A)
h.heapsort()

