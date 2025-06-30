class Queue:
    def __init__(self,size=100000):
        self.size=size
        self.arr=[]
    
    def __repr__(self):
        res=""
        for a in self.arr:
            res+=str(a)+" "
        return res    
    
    def push(self,v):
        if len(self.arr)>=self.size:
            raise ValueError
        self.arr.append(v)
        
    def pop(self):
        return self.arr.pop(0)
        
    def is_empty(self):
        return len(arr)==0
