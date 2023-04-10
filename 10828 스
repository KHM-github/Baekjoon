from sys import stdin
def input():
    return stdin.readline().rstrip()

class Stack:
    
    def __init__(self):
        self.stack=[]
        
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if len(self.stack)!= 0:
            print(self.stack[-1])
            self.stack.pop()
        else:
            print("-1")
        
    def size(self):
        print(len(self.stack))
    
    def empty(self):
        if len(self.stack)== 0:
            print("1")
        else:
            print("0")
        
    def top(self):
        if len(self.stack)== 0:
            print("-1")
        else:
            print(self.stack[-1])

N= int(input())
myStack= Stack()

for i in range(N):
   a= input().split()
   if a[0] == 'push':
       myStack.push(int(a[1]))
   elif a[0] == 'pop':
        myStack.pop()
   elif a[0] == 'size':
        myStack.size()
   elif a[0] == 'empty':
        myStack.empty()
   elif a[0] == 'top':
        myStack.top()
