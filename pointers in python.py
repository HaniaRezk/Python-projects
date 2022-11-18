class elem: #class pointers
    def __init__(self,keyvalue):
        self.key=keyvalue
        self.p=None
        self.left=None
        self.right=None
    def show(self):
        print("the value is", self.key,"its parent is", self.p,"the left child",self.left,"its right sibling", self.right)
        print(f"the value is {self.key}, its parent is {self.p}, the left child {self.left}, its right sibling {self.right}")

    def addRightChild(self,x): #left-child right sibling representation
        if self.left==None:
            self.left=x
        else:
            while self.right!=None:
                self=self.right
            self.right.key=x


    def showDescendants(self):
       self.show()
       if self.left!=None:
           self.left.showDescendants()
       if self.right!=None:
           self.right.showDescendants()

    def showleaves(self):
        if self.left==None:
            print(self.key)
        if self.left!=None:
            self.left.showleaves()
        if self.right!=None:
            self.right.showleaves()



class tree:
    def __init__(self,element):
        if element==None:
            self.root=None
        else:
            self.root=element

    def show1(self):
        self.root.showDescendants()

    def showleaves1(self):
        self.root.showleaves


